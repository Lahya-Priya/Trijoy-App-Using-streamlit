import streamlit as st
import numpy as np

def tic_tac_toe():
    st.title("Tic Tac Toe")
    st.write("Player X: You | Player O: AI")

    # Initialize the board in session state
    if "board" not in st.session_state:
        st.session_state.board = np.full((3, 3), "", dtype=str)  # Empty board
        st.session_state.current_player = "X"  # Player X starts

    def check_winner(board):
        # Check rows and columns for winner
        for i in range(3):
            if all(board[i, :] == "X") or all(board[:, i] == "X"):
                return "X"
            if all(board[i, :] == "O") or all(board[:, i] == "O"):
                return "O"
        # Check diagonals for winner
        if board[0, 0] == board[1, 1] == board[2, 2] != "":
            return board[0, 0]
        if board[0, 2] == board[1, 1] == board[2, 0] != "":
            return board[0, 2]
        if not np.any(board == ""):  # Check for draw
            return "Draw"
        return None

    def ai_move(board):
        empty_positions = np.argwhere(board == "")
        if empty_positions.size:
            return tuple(empty_positions[0])  # AI plays the first empty spot
        return None

    winner = check_winner(st.session_state.board)
    if winner:
        st.success(f"Game Over! Winner: {winner}")
    else:
        for i in range(3):
            cols = st.columns(3)  # Create 3 columns for each row of the board
            for j in range(3):
                cell_value = st.session_state.board[i, j] if st.session_state.board[i, j] else " "

                if cell_value == " ":  # Allow click if the cell is empty
                    if cols[j].button(" ", key=f"{i}-{j}"):  # Unique key for each button
                        st.session_state.board[i, j] = st.session_state.current_player
                        st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"
                        ai_position = ai_move(st.session_state.board)
                        if ai_position:
                            st.session_state.board[ai_position] = st.session_state.current_player
                        break  # After player move, AI plays
                else:
                    cols[j].button(cell_value, disabled=True, key=f"disabled-{i}-{j}")  # Disabled button
