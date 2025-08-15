select UP.id, P.name, UP."userID", R.name
from "UserProjects" UP
         inner join public."Roles" R on UP."roleID" = R.id
         inner join public."Projects" P on UP."projectID" = P.id
where UP."userID" in (
                      18348,
                      18350,
                      18352,
                      18347,
                      18349
    );


-- new user
select UP.id, P.name, UP."userID", U."firstName", R.name
from "UserProjects" UP
         inner join public."Roles" R on UP."roleID" = R.id
         inner join public."Projects" P on UP."projectID" = P.id
         inner join public."Users" U on UP."userID" = U.id
where P.id = 117;

select * from "Projects"
where id = 92;

select * from "UserProjects"
where "userID" = 1871;