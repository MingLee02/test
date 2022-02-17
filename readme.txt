Comments

So I think the test specification is quite vague.
I added a custom user model, because in my opinion it is easier to add this at the
start of a project rather than later on. 
The specification mentions users, so i origionally added the a user fk to the models, but upon asking. 
The response was that neigher a login or registration sytem is needed, so do i need to fk because a tester can
create a super user and login via the admin. I am taking a gamble and removing the user for now.
