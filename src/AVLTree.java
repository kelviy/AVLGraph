// Hussein's AVL Tree
// 2 April 2017
// Hussein Suleman
// reference: kukuruku.co/post/avl-trees/

public class AVLTree<dataType extends Comparable<? super dataType>> extends BinaryTree<dataType>
{
   private int insert_count = 0;
   private int search_count = 0;

   public int height ( BinaryTreeNode<dataType> node )
   {
      if (node != null)
         return node.height;
      return -1;
   }
   
   public int balanceFactor ( BinaryTreeNode<dataType> node )
   {
      return height (node.right) - height (node.left);
   }
   
   public void fixHeight ( BinaryTreeNode<dataType> node )
   {
      node.height = Math.max (height (node.left), height (node.right)) + 1;
   }
   
   public BinaryTreeNode<dataType> rotateRight ( BinaryTreeNode<dataType> p )
   {
      BinaryTreeNode<dataType> q = p.left;
      p.left = q.right;
      q.right = p;
      fixHeight (p);
      fixHeight (q);
      return q;
   }

   public BinaryTreeNode<dataType> rotateLeft ( BinaryTreeNode<dataType> q )
   {
      BinaryTreeNode<dataType> p = q.right;
      q.right = p.left;
      p.left = q;
      fixHeight (q);
      fixHeight (p);
      return p;
   }
   
   public BinaryTreeNode<dataType> balance ( BinaryTreeNode<dataType> p )
   {
      fixHeight (p);
      if (balanceFactor (p) == 2)
      {
         if (balanceFactor (p.right) < 0)
            p.right = rotateRight (p.right);
         return rotateLeft (p);
      }
      if (balanceFactor (p) == -2)
      {
         if (balanceFactor (p.left) > 0)
            p.left = rotateLeft (p.left);
         return rotateRight (p);
      }
      return p;
   }

   /**
    * Insert a new data item into the tree. The method would record the number of comparisons made.
    * @param d the data item to be inserted
    */
   public void insert ( dataType d )
   {
      root = insert (d, root);
   }
   /**
    * Insert a new data item into the tree. The method would record the number of comparisons made.
    * @param d the data item to be inserted
    * @param node the current node
    * @return
    */
   public BinaryTreeNode<dataType> insert ( dataType d, BinaryTreeNode<dataType> node )
   {    
      insert_count++;  
      if (node == null) {
         return new BinaryTreeNode<dataType> (d, null, null);
      }
      insert_count++; 
      if (d.compareTo (node.data) <= 0) {  
         node.left = insert (d, node.left);
      }
      else {    
         node.right = insert (d, node.right);
      }
      return balance (node);
   }
   
   public void delete ( dataType d )
   {
      root = delete (d, root);
   }   
   public BinaryTreeNode<dataType> delete ( dataType d, BinaryTreeNode<dataType> node )
   {
      if (node == null) return null;
      if (d.compareTo (node.data) < 0)
         node.left = delete (d, node.left);
      else if (d.compareTo (node.data) > 0)
         node.right = delete (d, node.right);
      else
      {
         BinaryTreeNode<dataType> q = node.left;
         BinaryTreeNode<dataType> r = node.right;
         if (r == null)
            return q;
         BinaryTreeNode<dataType> min = findMin (r);
         min.right = removeMin (r);
         min.left = q;
         return balance (min);
      }
      return balance (node);
   }
   
   public BinaryTreeNode<dataType> findMin ( BinaryTreeNode<dataType> node )
   {
      if (node.left != null)
         return findMin (node.left);
      else
         return node;
   }

   public BinaryTreeNode<dataType> removeMin ( BinaryTreeNode<dataType> node )
   {
      if (node.left == null)
         return node.right;
      node.left = removeMin (node.left);
      return balance (node);
   }

   /**
    * Find a data item in the tree. The method would record the number of comparisons made.
    * @param d the data item to be found
    * @return
    */
   public BinaryTreeNode<dataType> find ( dataType d )
   {
      search_count++;
      if (root == null)
         return null;
      else
         return find (d, root);
   }
   /**
    * Find a data item in the tree. The method would record the number of comparisons made.
    * @param d the data item to be found
    * @param node the current node
    * @return
    */
   public BinaryTreeNode<dataType> find ( dataType d, BinaryTreeNode<dataType> node )
   {
      search_count++;
      if (d.compareTo (node.data) == 0) {
         return node;
      }
      else if (d.compareTo (node.data) < 0) {
         search_count++;
         return (node.left == null) ? null : find (d, node.left);
      }
      else {
         search_count++;
         return (node.right == null) ? null : find (d, node.right);
      }
   }
   
   public void treeOrder ()
   {
      treeOrder (root, 0);
   }
   public void treeOrder ( BinaryTreeNode<dataType> node, int level )
   {
      if (node != null)
      {
         for ( int i=0; i<level; i++ )
            System.out.print (" ");
         System.out.println (node.data);
         treeOrder (node.left, level+1);
         treeOrder (node.right, level+1);
      }
   }

   public int getInsertCount() {
      int count = insert_count;
      insert_count = 0;
      return count;
   }

   public int getSearchCount() {
      int count = search_count;
      search_count = 0;
      return count;
   }

   public void clearCount() {
      insert_count = 0;
      search_count = 0;
   }
}

