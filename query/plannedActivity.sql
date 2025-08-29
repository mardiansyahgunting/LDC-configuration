-- check planned Activity
select "userID", "firstName" as Users, count(*) as Total_plots
from "PlannedActivities" PA
         inner join public."Users" U on PA."userID" = U.id
where "userID" in (
                   18349,
                   18350,
                   18352,
                   18347
    )
  and PA.status = 'planned'
group by "userID", "firstName";

-- Just check Bawon Plots
select "firstName" as Users, PA.id
from "PlannedActivities" PA
         inner join public."Users" U on PA."userID" = U.id
         inner join public."Plots" P on PA."plotID" = P.id
where "userID" in (
                   18349,
                   18350,
                   18352,
                   18347
    )
  and PA.status = 'planned'
  and P."plotVillage" not in ('BASUNGAN');


-- new user
select *
from "PlannedActivities"
where "userID" = 18348
  and status = 'planned';



select *
from "PlannedActivities"
where "userID" in (
    18349
    )
  and status = 'planned';


-- Remove Planned Activity on non Basungan Village

select *
from "PlannedActivities" PA
         inner join public."Plots" P on PA."plotID" = P.id
where "userID" in (
                   18352,
                   18347
    )
  and "plotVillage" NOT IN ('BASUNGAN')
  and PA.status = 'planned';