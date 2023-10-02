class node:
  def __init__(self, key):
    self.key = key
    self.height = 1
    self.left = None
    self.right = None

def height(node):
  if node is None:
    return 0
  else:
    l = height(node.left)
    r = height(node.right)
    node.height = 1 + max(l, r)
    return node.height

def balanceFactor(node):
  if node is None:
    return 0
  return height(node.left) - height(node.right)

def leftRotate(z):
  y = z.right
  T2 = y.left
  y.left = z
  z.right = T2
  z.height = 1 + max(height(z.left), height(z.right))
  y.height = 1 + max(height(y.left), height(y.right))
  return y

def rightRotate(z):
  y = z.left
  T3 = y.right
  y.right = z
  z.left = T3
  z.height = 1 + max(height(z.left), height(z.right))
  y.height = 1 + max(height(y.left), height(y.right))
  return y

def minValueNode(root):
  if root is None or root.left is None:
    return root
  return minValueNode(root.left)


def insert(root, key):
  if root is None:
    return node(key)
  else:
    if key < root.key:
      root.left = insert(root.left, key)
    else:
      root.right = insert(root.right, key)

  root.height = height(root)
  balanceFac = balanceFactor(root)
  
  if balanceFac > 1:
    if balanceFactor(root.left) >= 0:
      return rightRotate(root)
    else:
      root.left = leftRotate(root.left)
      return rightRotate(root)
  if balanceFac < -1:
        if balanceFactor(root.right) <= 0:
          return leftRotate(root)
        else:
          root.right = rightRotate(root.right)
          return leftRotate(root)
  return root

def delete(root, key):
  if not root:
    return root
  elif key < root.key:
    root.left = delete(root.left, key)
  elif key > root.key:
    root.right = delete(root.right, key)
  else:
    if root.left is None:
      temp = root.right
      root = None
      return temp
    elif root.right is None:
      temp = root.left
      root = None
      return temp
    temp = minValueNode(root.right)
    root.key = temp.key
    root.right = delete(root.right, temp.key)
  if root is None:
      return root

  root.height = height(root)
  balanceFac = balanceFactor(root)

  if balanceFac > 1:
    if balanceFactor(root.left) >= 0:
      return rightRotate(root)
    else:
      root.left = leftRotate(root.left)
      return rightRotate(root)
  if balanceFac < -1:
    if balanceFactor(root.right) <= 0:
      return leftRotate(root)
    else:
      root.right = rightRotate(root.right)
      return leftRotate(root)
  return root

def search(root, key):
  if root is None:
    print("Valor não encontrado!")
    return False
  else:
    if root.key == key:
      print("Valor encontrado!")
      return root
    else:
      if key < root.key:
        return search(root.left, key)
      else:
        return search(root.right, key)

if __name__ == "__main__":
  root = None
  root = insert(root, 2)
  root = insert(root, 3)
  #falta retornar corretamente o nodo, não a raiz
