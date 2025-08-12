-- check planned Activity
select *
from "PlannedActivities"
where "userID" in (
                   1360,
                   18348,
                   18350,
                   18352,
                   18347
    )
  and status = 'planned';

-- new user

select *
from "PlannedActivities"
where "userID" in (
    18349
    )
  and status = 'planned';