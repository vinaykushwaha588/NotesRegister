First you need to create virtual Environment after intall requrements.txt

API
POST api/notes/: Create a new note.
GET api/notes/<int:pk>/: Fetch a note by its primary key.
GET api/notes-substring/?title=line in large  Query notes by title substring.
PUT api/notes/<int:pk>/: Update an existing note.
