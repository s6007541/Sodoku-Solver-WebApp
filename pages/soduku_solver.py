import streamlit as st

st.markdown("""
    # Sodoku Solver
    This app can solves any valid Sodoku Problem
    ***
         """)
st.sidebar.markdown("# Main page 👀")

M = 9
def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j],end = " ")
        print()
def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
             
    for x in range(9):
        if grid[x][col] == num:
            return False
 
 
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
def Suduko(grid, row, col):
 
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
     
        if solve(grid, row, col, num):
         
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False


def print_table(grid):
  grid2 = []
  for j in range(9):
    grid2.append([i if i != 0 else "" for i in grid[j]])
  style_td = """
      td {<!--from  w  w  w .  j av  a 2 s .  c om-->
      width: 50px;
      height: 50px;
      border: 1px solid #000;
      text-align: center;
    }"""
  style_tr = """
    td:nth-of-type(3n) {
      border-right: 3px solid #95C7F1 !important;
    }
    tr:nth-of-type(3n) td {
      border-bottom: 3px solid #95C7F1 !important;
    }"""
  style_table = """table {
      border: 3px solid #95C7F1 !important;
      width: 450px;
      height: 450px;
      margin-left: auto;
      margin-right: auto;
      }"""
    
  st.markdown("<style>" + style_td + style_tr + style_table + "</style>", unsafe_allow_html=True)

  st.markdown("""
    <table cellpaddibg="0" cellspacing="0" > 
    <tbody> 
      <tr> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      </tr> 
      <tr> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      </tr> 
      <tr> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      </tr> 
      <tr> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      </tr> 
      <tr> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      </tr> 
      <tr> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      </tr> 
      <tr> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      </tr> 
      <tr> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      </tr> 
      <tr> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      <td>{}</td> 
      </tr> 
    </tbody> 
    </table>  """.format(grid2[0][0],grid2[0][1],grid2[0][2],grid2[0][3],grid2[0][4],grid2[0][5],grid2[0][6],grid2[0][7],grid2[0][8],
                         grid2[1][0],grid2[1][1],grid2[1][2],grid2[1][3],grid2[1][4],grid2[1][5],grid2[1][6],grid2[1][7],grid2[1][8],
                         grid2[2][0],grid2[2][1],grid2[2][2],grid2[2][3],grid2[2][4],grid2[2][5],grid2[2][6],grid2[2][7],grid2[2][8],
                         grid2[3][0],grid2[3][1],grid2[3][2],grid2[3][3],grid2[3][4],grid2[3][5],grid2[3][6],grid2[3][7],grid2[3][8],
                         grid2[4][0],grid2[4][1],grid2[4][2],grid2[4][3],grid2[4][4],grid2[4][5],grid2[4][6],grid2[4][7],grid2[4][8],
                         grid2[5][0],grid2[5][1],grid2[5][2],grid2[5][3],grid2[5][4],grid2[5][5],grid2[5][6],grid2[5][7],grid2[5][8],
                         grid2[6][0],grid2[6][1],grid2[6][2],grid2[6][3],grid2[6][4],grid2[6][5],grid2[6][6],grid2[6][7],grid2[6][8],
                         grid2[7][0],grid2[7][1],grid2[7][2],grid2[7][3],grid2[7][4],grid2[7][5],grid2[7][6],grid2[7][7],grid2[7][8],
                         grid2[8][0],grid2[8][1],grid2[8][2],grid2[8][3],grid2[8][4],grid2[8][5],grid2[8][6],grid2[8][7],grid2[8][8],), unsafe_allow_html=True)





with st.form(key = 'form1'):
    ''' 0 is blank '''
    inputdata = [int(i) for i in st.text_input(label="", placeholder='020000087860020400004010000000063200570900600200500900010090000008000004000047000', max_chars=None, key='1')]

    submitted = st.form_submit_button(label = "Submit")
    if(submitted):
        grid = []
        grid.append(inputdata[:9])
        grid.append(inputdata[9:18])
        grid.append(inputdata[18:27])
        grid.append(inputdata[27:36])
        grid.append(inputdata[36:45])
        grid.append(inputdata[45:54])
        grid.append(inputdata[54:63])
        grid.append(inputdata[63:72])
        grid.append(inputdata[72:81])
        st.markdown("""
          ### Your Input Grid
              """)
        print_table(grid)

        
        if (Suduko(grid, 0, 0)):
            puzzle(grid)
            st.markdown("""
              ***
              ### Solution
                  """)
            print_table(grid)
            
            
        else:
            st.markdown("""
              ***
              ### Solution does not exist! Please check your input again.
                  """)

            
