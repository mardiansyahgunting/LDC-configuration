select *
from "Projects"
where name like '%LDC%'


select "plotVillage", count(*)
from "PlotProjects" PP
         inner join public."Plots" P on PP."plotID" = P.id
where "projectID" = 117
group by "plotVillage";