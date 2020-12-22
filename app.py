import random
import re
from itertools import product

import streamlit as st
import pandas as pd
import numpy as np
from suduko_solver import solve_suduko
from ui_auxiliary import empty_board_str, board_matrix_to_dataframe

random.seed(0)

st.title("Suduko Solver")

st.subheader("Use linear programming to solve a Suduko puzzle.")

input_data = st.text_area(
    label="Enter the starting state of the board.", value=empty_board_str, height=400
)

rows = np.repeat(np.arange(1, 10), 9)
cols = np.tile(np.arange(1, 10), 9)
values = []

for line in input_data.split("\n"):
    if not "-" in line:
        vals = re.findall("[0-9]", line.rstrip())
        values += [int(x) for x in vals]

if len(rows) == len(cols) == len(values):

    known_cells = pd.DataFrame({"i": rows, "j": cols, "k": values})

    board = pd.DataFrame(product(range(1, 10), range(1, 10)), columns=["i", "j"])
    board = pd.merge(board, known_cells, how="left")
    board.k = ["" if np.isnan(x) else str(int(x)) for x in board.k]
    board = board.pivot(index="i", columns="j", values="k")

    if st.button("Solve!"):
        st.markdown("**Solution**")
        # st.markdown(board_as_markdown_table(board))
        st.write(board_matrix_to_dataframe(np.random.randint(1, 10, (9, 9))))
    else:
        st.markdown("**Board layout**")
        st.write(board)


else:
    st.write("Something is wrong with the layout of the board. Please try again.")
