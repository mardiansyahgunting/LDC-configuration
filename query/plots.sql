select *
from "Projects"
where name like '%LDC%'


select P.id, P."plotName" from "PlotProjects" PP
inner join public."Plots" P on PP."plotID" = P.id
where "projectID" = 117;


select "plotVillage", count(*)
from "PlotProjects" PP
         inner join public."Plots" P on PP."plotID" = P.id
where "projectID" = 117
group by "plotVillage";