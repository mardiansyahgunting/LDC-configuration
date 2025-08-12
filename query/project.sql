-- Org

    select id, name, country from "Organizations"
    where name like '%LDC%';

-- Proj

    select id, name, "projectStatus" from "Projects"
    where "organizationID"  = 57;


-- Roles

    select id, name from "Roles"
    where name = 'Forester'
    and "organizationID" = 57;


-- get all Roles

    select * from "Roles"
    where "organizationID" = 57;

select * from "Projects"
where id in (88);