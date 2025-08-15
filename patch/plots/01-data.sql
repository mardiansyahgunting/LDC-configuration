select "plotAdditionalData" ->> 'enumer' from "PlotProjects" PP
inner join public."Plots" P on PP."plotID" = P.id
where "projectID" = 117
group by "plotAdditionalData" ->> 'enumer';
;





select * from "Projects"
where name like '%LDC%';

select * from "Users"
where email like '%LDC%';



select "plotID", "plotName" from "PlotProjects" PP
inner join public."Plots" P on PP."plotID" = P.id
where "projectID" = 117;
