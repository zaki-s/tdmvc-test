

For the running of the tests set up the virtual environment, 
install deoendencies listed in requirements.txt,
to run tests for individual functions of the todoMVC app,
    run the code form the terminal to individually run the add,
     complete, delete function.

Next cd into the "TOTEST" to be in the same directory as the test files

  For the opening of the app run
                     "pytest tests/test_open_app.py -s"

  For the adding of a new todo item run
                     "pytest tests/test_add_todo.py -s"

  For the completeion of a new todo item run
                     "pytest tests/test_complete_todo.py -s"

  For the filtering of the todo items run
                     "pytest tests/test_filter_todo.py -s"

  For the deleting of a todo item run
                     "pytest tests/test_delete_todo.py -s"
      
      To run alll the tests make sure youve installed dependencies
         and then proceed to run
                     "pytest"
