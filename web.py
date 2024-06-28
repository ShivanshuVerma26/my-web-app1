import streamlit as st
import functions as fs

todos = fs.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    fs.write_todos(todos)


st.title("My Todo App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fs.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input("", "Add a new Todo...",
              on_change=add_todo, key="new_todo")

