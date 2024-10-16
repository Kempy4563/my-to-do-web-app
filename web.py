import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    local_todo = st.session_state["new_todo"] + "\n"
    print(local_todo)
    todos.append(local_todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app will increase your productivity")

#get index of the checked todos and remove the todos that are checked and write new todos to todos.txt
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)

        #delete the checked items from the session state
        del st.session_state[todo]

        #needed when working with checkboxes
        st.rerun()


st.text_input(label="Enter..", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

#show session state on the web page
#st.session_state

