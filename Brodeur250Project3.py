#Brianna Brodeur
#COMP 250 Project 3: Student Directory 

from collections import deque

#Class declaration

#Declares attributes for student directory nodes
class student:
    def __init__(self,id,name,major):
        self.id = id
        self.name = name
        self.major = major
        self.left = None
        self.right = None

#--------------------------------------------------------------------------------------------
#Binary Search Tree
#Contains root and methods: insert, search, traversals (DFS and BFS), and tree stats
#Methods and Functions without the '_' tag are called in the main(). This allows the BST to use values and attributes assigned outside of it properly.
class BinarySearchTree:

    #Creates the root attribute in the BST.
    def __init__(self):
       self.root = None

    #The insert function used to add students into the directory
    def insert(self,id,name,major):
        #If there is no root, set the root as an instance of the student directory class.
        if (self.root) is None:
            self.root = student(id,name,major)
        #If the root has already been established, go through the actions in the _insert function.
        else: 
            self._insert (self.root, id,name,major)

        #This function places every student into the directory besides the root student.
    def _insert(self,root,id,name,major):
        #This checks for duplicates:
        #If the ID of the student provided is the same as the ID of another student, print the matching student's information.
        if id == root.id:
            print(f"{root.name}, student ID {root.id}, is a {root.major} major")
            return 

        #These determine where the student will be placed in the BST's structure.
        #If the provided ID is less than the root, check if the left space underneath it is empty.
        if id < root.id:
            #If the left is unoccupied, set the lower ID to the left side.
            if root.left is None:
                root.left = student(id,name,major)
            #If the left space is already occupied, call the function again using the left side as the 'root' in comparison to insert it
            #below.
            else:
                self._insert(root.left, id,name,major)
        #If the provided ID is higher, run the same check for the right side.
        else:
            #If the right is empty, place the ID in the right side.
            if root.right is None:
                root.right = student(id,name,major)
            #If not, place it under the student occupying the right space.
            else:
                self._insert(root.right, id,name,major)
#--------------------------------------------------------------------------------------
#Search method
#The search method is used to search for a specific student in the directory using their ID as the target
    #Call search method using the BST's root and the target from the user
    def search(self,id):
        return self._search(self.root,id)
    #True search method
    def _search(self,root,id):
        #Set the amount of students in the directoy as 0 initially.
        #This keeps track of each student visited before the target is found.
        count = 0

        #If the root is empty, return.
        if root is None:
            return
        #Declare stack which contains a student (starts with the root).
        #Append the root (current student) to the stack after each iteration
        stack = [root]
        #While the stack has a student or students in it, proceed:
        while stack:
            #'Root' acts as the current student being checked. 
            #The 'root' changes to the student added last into the stack (which is also removed)
            root = stack.pop()

            #If the current student has another student to the right-under side of them, add the right student to the stack.
            #Move on
            if root.right:
                stack.append(root.right)
            #If the current student has another student to the left-under side of them, add the left student to the stack.
            #Move on
            if root.left:
                stack.append(root.left)
            #If the ID of the current student matches the target ID, return the number of students visited before
            #The found student, and print the information of the found student. 
            if root.id == id:
                print("Number of students visited:", count)
                print("Student found!")
                print(f"{root.name}, student ID {root.id}, is a {root.major} major")
                #Return and end
                return
            #During each iteration, print the visted student's ID, name, and major.
            visited = f"ID: {root.id} | Name: {root.name} | Major: {root.major}"
            print(visited)
            #Count each student visited.
            count += 1
        #Once the stack is empty and the current student has no left or right nodes and no matches, 
        #Return the number of students visited (should be every student in the directory)
        #And print that the student has not been found.
        print("Number of students visited:", count)
        print("Student not found.")
        #The function returns and ends
        return


#DFS-----------------------------------------------------------

#pre-order Traversal
    def preOrderTraversal(self,id):
        return self._preOrderTraversal(self.root,id)

    #Traverses through the student directory tree in Pre-Order (root,left,right)
    def _preOrderTraversal(self,root,id):
        if root is None:
             return
        #Print the root first
        print(root.id, root.name, root.major)
        #Call the function again with the left-side student as the root
        self._preOrderTraversal(root.left,root.id)
        #Call the function again with the root-side student as the root
        self._preOrderTraversal(root.right,root.id)

 #in-order traversal
    def inOrderTraversal(self,id):
        return self._inOrderTraversal(self.root,id)
    
#Traverses through the student directory in-Order (left,root,right) 
    def _inOrderTraversal(self,root,id):
        if root is None:
            return
        
        self._inOrderTraversal(root.left,root.id)
        print(root.id, root.name, root.major)
        self._inOrderTraversal(root.right,root.id)

#post-order
    def postOrderTraversal(self,id):
        return self._postOrderTraversal(self.root, id)
    
#Traverse through the student directory in post-order(left,right,root)    
    def _postOrderTraversal(self,root,id):
        if root is None:
            return
        
        self._postOrderTraversal(root.left,root.id)
        self._postOrderTraversal(root.right,root.id)
        print(root.id, root.name, root.major)

#BFS
    def bfsTraversal(self,id):
        return self._bfsTraversal(self.root,id)
    
#Breadth-First Traversal goes through student directory by level.
    def _bfsTraversal(self,root,id):
        #The levels variable keeps track as the number of levels.
        levels = 0
        if root is None:
            return
        #The result list is created in order to properly display the levels at the end of the traversal
        result = []
        #A queue is created, this queue will be used to keep track of the current student being looked at, similar to the stack in the 
        #search function.
        q = deque()
            #Append the root to start
        #Stores the current student in the queue, starting with the root student.
        q.append(root)

        #While the queue contains a student (i.e. there's a student in the directory)
        while q:
            #The size of the level is determined by the number of students in the queue
            level_size = len(q)
            #Stores the students in each level and resets once moved onto a new level.
            current_level = []
            #Counts each level
            levels += 1

            #For the amount of students in each level
            for _ in range(level_size):
                #Set the current student to the student last added to the queue (remove from queue)
                student = q.popleft()
                #Append the student to the current level
                current_level.append(str(f"ID: {student.id} | Name: {student.name} | Major: {student.major}"))
                
                #Adds student under the left side of the current student to the queue if there is a student present
                if student.left:
                    q.append(student.left)
                #Adds student under the right side of the current student to the queue if there is a student present
                if student.right:
                    q.append(student.right)
            #Formats the current_level as a string
            level = " ".join(current_level)
            #Appends the current level to the result string for formatting purposes
            result.append(str(f"Level {levels}: {level}"))
        #Prints each level on their own respective line once the directory has been traversed through completely, 
        #And the queue is emptied one final time.
        for item in result:
            print(item)
#-------------------------------------------------------------------------
#Tree stats:

#Number of students
    def count_students(self,id):
        return self._count_students(self.root,id)
    
    #Counts the amount of students in the directory     
    def _count_students(self,root,id):
        if root is None:
            return 0
        #Sets the amount of students to 1 by default. If there are none, 0 is returned (but the message clarifying the lack of students is printed first.)
        total_students = 1
        #Returns the sum of initial amount of total_students, student nodes to the left and student nodes to the right with recursion
        return total_students + self._count_students(root.left,root.id) + self._count_students(root.right,root.id)
    
#Tree height
    def tree_height(self,id):
        return self._tree_height(self.root,id)
    #Gets the tree height (number of levels in the tree)

    def _tree_height(self,root,id):
        if root is None:
            return 0
        #Takes the height of the left side by calling the function again with the left student nodes
        left_height = self._tree_height(root.left,root.id)
        #Takes the height of the right side by calling the function again with the right student nodes
        right_height = self._tree_height(root.right,root.id)
        #Returns the sum of 1 (for the root) with the largest value between the left and right heights
        return 1 + max(left_height,right_height)
    
#Smallest ID
    def get_min_student(self,id):
        return self._get_min_student(self.root,id)
    #Finds the smallest ID value in the student directory  

    def _get_min_student(self,root,id):
        if root is None:
            return float ('inf')
        #Takes the smallest of the left student nodes
        left_min = self._get_min_student(root.left,root.id)
        #Takes the smallest of the right student nodes
        right_min = self._get_min_student(root.right,root.id)

        #Returns the minimum value of the left and right student notes
        return min(root.id,left_min, right_min)

#Highest ID
    def get_max_student(self,id):
        return self._get_max_student(self.root,id)
    #Finds the largest ID value in the student directory
    def _get_max_student(self,root,id):
        if root is None:
            return float ('-inf')
        
        #Takes the largest of the left student nodes
        left_max = self._get_max_student(root.left,root.id)
        #Takes the largest of the right student nodes
        right_max = self._get_max_student(root.right,root.id)

        #Returns the largest ID value of the left and right student notes 
        return max(root.id,right_max, left_max)


#---------End of Binary Search Tree----------------------------------
#----------------------------------------------

#Check for integer
#Integer Exception:
#Ensures that the input for the menu is within range and that the input is an integer
def check_selected(prompt, low, high):
    while True:
        #Checks that the input is within the low and high range (if the value type is an integer)
        try:
            x = int(input(prompt))
            #If too low, inform the user and recall the intial prompt
            if x < low:
                print("Number is too low!")
                return check_selected(prompt,low, high)
            if x > high:
                #If too high, inform the user and recall the initial prompt
                print("Number is too high!")
                return check_selected(prompt,low,high)
            return x
        #If the value type is not an integer...
        except ValueError:
            #Ask the user to enter an integere and recall the initial prompt
            print("Please enter an integer.")
            return check_selected(prompt,low,high)
        
#Checks that the ID input is an integer value          
def check_id(prompt):
    #If so, return the input value
    try:
        x = int(input(prompt))
        return x
    #If the value type is not an integer, inform user and re call the initial prompt.
    except ValueError:
        print("Please enter an integer.")
        return check_id(prompt)

#Function that takes the id, name, and major given by the user to create a student that is added to the student directory
def add_student(tree,id,name,major):
     tree.insert(id,name,major)
#--------------------------------------------------------------------------------
#Main program 
def main():
    #Creates the Binary Search Tree instance to be refered to
    bst = BinarySearchTree()

    #Allows the menu to reprint itself until user says otherwise
    done = False


    #Main Menu:
    while not done:
        print("\t--------Student Directory------------\n")
        print("1. Add new student\n")
        print("2. Search for student by ID \n")
        print("3. Display all students with with DFS\n")
        print("4. Display all students with BFS \n")
        print("5.Display tree stats (total number of students)\n")
        print("6. Display student with the smallest ID and student with the largest ID \n")
        print("7.Exit")

        #Prompts the user to select an option in the menu.
        selected = check_selected("Choose an option (1-7): ", 1, 7)

        #--------------------------------------------Add student---------------------------------------
        #Adds new student to the directory given by the user
        if selected == 1:
            print("\t------Add Student-----\n")
            id = check_id("Enter the student's ID: ")
            name = input("Enter the student's name: ")
            major = input("Enter the student's major: ")
            
            add_student(bst,id,name,major)
        #--------------------------------------Find student in directory----------------------------
        #Looks for a student in the directory by their ID provided by the user
        if selected == 2:
            print("\t------Find Student By ID-----\n")
            target = check_id("Enter the ID of the student you'd like to look for: ")

            #Try and Except that informs the user if the student directory is empty.
            try:
                print("Visited students: ")
                (bst.search(target))
            except UnboundLocalError:
                print("No students in the directory yet!")

                
        #--------------------------------------Choose DFS display---------------------------------------
        #Gives the user the option to choose how they would like to traverse through the directory (i.e. how they would like to display the contents)
        if selected == 3:
            #while statement allows the question to be re-prompted if an invalid answer is given
            print("\t-------Choose DFS Order to Display Directory In----------\n")
            while True:
                traversal_choice = input("Would you like to view the student directory in Pre-Order, In-Order, or Post-Order Traversal: ")

                #Display in pre-order traversal
                if traversal_choice == "Pre-Order":
                    try:
                        print("Pre-Order:\n")
                        bst.preOrderTraversal(id)
                    #Returns message if student directory is empty
                    except UnboundLocalError:
                        print("No students in the directory yet!")
                    break
                #Display in in-order traversal
                if traversal_choice == "In-Order":
                    try:
                        print("In-Order\n")
                        bst.inOrderTraversal(id)
                    except UnboundLocalError:
                        print("No students in the directory yet!")
                    break
                #display in post-order traversal
                if traversal_choice == "Post-Order":
                    try:
                        print("Post-Order\n")
                        bst.postOrderTraversal(id)
                    except UnboundLocalError:
                        print("No students in the directory yet!")
                    break
                #If something other than the 3 options is given, tell the user and ask again until a valid answer is provided.
                else:
                    print("Choose from the 3 options.")
                    

        #-----------------------------------------BFS display----------------------------------------
        #Displays student directory in BFS order
        if selected == 4:
            print("\t------Display Student Directory in BFS Order-------\n")
            try:
                bst.bfsTraversal(id)
            #Notify user if the directory is empty
            except UnboundLocalError:
                print("No students in the directory yet!")

        #--------------------------------------------Tree Stats 1 (num of students and tree height)----------------------------
        #Returns the number of students and the height of the tree
        if selected == 5:
            print("\t----------TREE STATS 1-------\n")
            try:
                print(f"Number of students: {bst.count_students(id)}")
                
                print(f"Tree height: {bst.tree_height(id)}")
            #Notify user if directory is empty.
            except UnboundLocalError:
                print("No students in the directory yet!")
        #----------------------------------------Tree Stats 2 (smallest and largest ID)-----------------------------------
        #Returns the student with the smallest ID and the student with the largest ID
        if selected == 6:
            print("\t-------TREE STATS 2-------\n")
            try:
                print(f"Smallest ID in directory: {bst.get_min_student(id)}")
                print(f"Largest ID in directory: {bst.get_max_student(id)}")
            #Notify the user if directory is empty
            except UnboundLocalError:
                print("No students in the directory yet!")
        #---------------------------------------------EXIT PROGRAM--------------------------
        #Exits program by stopping the run of the menu
        if selected == 7:
            print("Exiting student directory.")
            done = True

#Call-------------------------------------
main()




#Questions:
#1. Searching a balanced BST is O(log n) because the left and right sides are even, therefore the number of nodes (n) will double on each level.
#Because of this, the amount of moves made down the tree while looking for the targeted value is only increased by 1 as the tree halves itself.
#Meanwhile, in an unbalanced tree, the time complexity is o(n) because it traverses in a linear pattern which is solely reliant on the amount of nodes within the tree,
#as opposed to the number of nodes and the doubling of nodes per-level that cuts the work in half with each traverse.

#2. Building a balanced tree is O(nlogn) because the amount of work to complete every insertion of a student is determined by the height of the tree (O (log n)). This process must be done the same amount of times as the number of students 
#within the tree (n), so the three are multiplied. 
#If n = 1,000 students: O(log n)= log(1,000) = 9.966
#1,000 x 9.966 = 9,966. So the number of steps of O(n log n), where n = 1,000 is 9,966 which is nearly 10,000.










