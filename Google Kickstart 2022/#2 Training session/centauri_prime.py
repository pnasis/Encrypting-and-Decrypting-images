# TODO: Complete the get_ruler function
def get_ruler(kingdom):
  ruler = ''
  name = kingdom
  w_list = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
  string_tuple = tuple(w_list)
  if name.endswith(string_tuple):
    ruler='Alice'
  elif name.endswith('y') or name.endswith('Y'):
    ruler='nobody'
  else:
    ruler='Bob'
    
  return ruler

def main():
  # Get the number of test cases
  T = int(input())
  for t in range(T):
    # Get the kingdom
    kingdom = input()
    print('Case #%d: %s is ruled by %s.' % (t + 1, kingdom, get_ruler(kingdom)))

if __name__ == '__main__':
  main()
