-- check planned Activity
select "userID", count(*)
from "PlannedActivities"
where "userID" in (
                   18349,
                   18350,
                   18352,
                   18347
    )
  and status = 'planned'
group by "userID";

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