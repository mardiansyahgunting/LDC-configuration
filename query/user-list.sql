-- https://docs.google.com/spreadsheets/d/1HyCxkdHvO1zD9teeX6R2fsUR23hUBYYqCakN2afxOMQ/edit?gid=0#gid=0

select id, "phoneNumber", "firstName", "lastName", "isActive"
from "Users"
where "phoneNumber" in (
      '6282374858771',
      '6285609133465',
      '6281367414456',
      '6283897183458',
      '6281119920406'
    );

-- list Users New

select id, "phoneNumber", "firstName", "lastName", "isActive"
from "Users"
where "phoneNumber" in (
      '6281367444156'
    );