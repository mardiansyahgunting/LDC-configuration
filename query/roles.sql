select UP.id, P.name, UP."userID", R.name
from "UserProjects" UP
         inner join public."Roles" R on UP."roleID" = R.id
         inner join public."Projects" P on UP."projectID" = P.id
where UP."userID" in (
                      18348,
                      18350,
                      18352,
                      18347
    );


-- new user
select UP.id, P.name, UP."userID", R.name
from "UserProjects" UP
         inner join public."Roles" R on UP."roleID" = R.id
         inner join public."Projects" P on UP."projectID" = P.id
where UP."userID" in (
    18349
    );