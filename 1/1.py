# 定义二叉树结点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 先序遍历
def preorderTraversal(root):
    if not root:
        return
    print(root.val, end=" ")
    preorderTraversal(root.left)
    preorderTraversal(root.right)

# 中序遍历
def inorderTraversal(root):
    if not root:
        return
    inorderTraversal(root.left)
    print(root.val, end=" ")
    inorderTraversal(root.right)

# 后序遍历
def postorderTraversal(root):
    if not root:
        return
    postorderTraversal(root.left)
    postorderTraversal(root.right)
    print(root.val, end=" ")

# 建立二叉树
def buildTree():
    val = input("请输入结点的值（输入#表示空结点）：")
    if val == '#':
        return None
    root = TreeNode(int(val))
    root.left = buildTree()
    root.right = buildTree()
    return root

# 主函数
if __name__ == '__main__':
    # 建立二叉树
    root = buildTree()

    # 先序遍历
    print("先序遍历结果为：")
    preorderTraversal(root)
    print()

    # 中序遍历
    print("中序遍历结果为：")
    inorderTraversal(root)
    print()

    # 后序遍历
    print("后序遍历结果为：")
    postorderTraversal(root)
    print()
