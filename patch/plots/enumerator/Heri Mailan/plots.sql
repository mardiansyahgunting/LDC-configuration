-- get the users Detail
select *
from "Users"
where id in (
             18350,
             18352,
             18347,
             18349
    );

-- get all of Enumerator
select "plotAdditionalData" ->> 'enumer'
from "PlotProjects" PP
         inner join public."Plots" P on PP."plotID" = P.id
where "projectID" = 117
group by "plotAdditionalData" ->> 'enumer';

-- Specific Plots
select "plotID", "plotName", "plotAdditionalData" ->> 'enumer'
from "PlotProjects" PP
         inner join public."Plots" P on PP."plotID" = P.id
where "projectID" = 117
  and "plotAdditionalData" ->> 'enumer' = 'Heri Mailan';