import streamlit as st
import todos_functions


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    todos_functions.write_todos(todos)


st.title("My TODO App")

todos = todos_functions.get_todos()

for index, todo in enumerate(todos):
    chk_box = st.checkbox(todo, key=todo)
    if chk_box:
        todos.pop(index)
        todos_functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo..", on_change=add_todo, key="new_todo")
