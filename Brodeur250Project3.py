#Brianna Brodeur
#COMP 250 Project 3: Student Directory 

from collections import deque

#Class declaration
class student:
    def __init__(self,id,name,major):
        self.id = id
        self.name = name
        self.major = major
        self.left = None
        self.right = None

#--------------------------------------------------------------------------------------------
#Binary Search Tree
class BinarySearchTree:

    def __init__(self):
       self.root = None

    def insert(self, id,name,major):
        if (self.root) is None:
            self.root = student(id,name,major)
        else:
            self._insert (self.root, id,name,major)

    def _insert(self,root,id,name,major):
        if id == root.id:
            print(f"{root.name}, student ID {root.id}, is a {root.major} major")
            return
        if id < self.root.id:
            if root.left is None:
                root.left = student(id,name,major)
            else:
                self._insert(root.left, id,name,major)
        else:
            if root.right is None:
                root.right = student(id,name,major)
            else:
                self._insert(root.right, id,name,major)
#--------------------------------------------------------------------------------------
#Search method
    def search(self,root, id):
        count = 0
        
        if root is None:
            return
        stack = [root]
        while stack:
            root = stack.pop()
            
            visited = root.id
            print(visited)
            count += 1
            
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            if root.id == id:
                print("Number of students visited:", count)
                return True
        else:
            print("Number of students visited:", count)
            return False


#DFS-----------------------------------------------------------

#pre-order Traversal
    def preOrderTraversal(self,root,id):
        if self.root is None:
             return
        
        print(self.root.id, self.root.name, self.root.major)
        self.preOrderTraversal(root.left,self.root.id)
        self.preOrderTraversal(root.right,self.root.id)

 #in-order traversa
    def inOrderTraversal(self,root):
        if root is None:
            return
        
        self.inOrderTraversal(root.left,id)
        print(root.id, root.name, root.major)
        self.inOrderTraversal(root.right,id)

#post-order
    def postOrderTraversal(self,root,id):
        if root is None:
            return
        
        self.postOrderTraversal(root.left)
        self.postOrderTraversal(root.right)
        print(root.id, root.name, root.major)

#BFS
    def bfsTraversal(self,root,id,name,major):
        levels = 0
        if root is None:
            return
            #Create queue to keep track of students
        q = deque()
            #Append the root to start
        q.append(root)
        while q:
            #The length of the level is how long the queue is before
            #moving onto the next level
            level_size = len(q)
            #Brackets to store the students in each level
            current_level = []
            for _ in range(level_size):
                #Remove student from storage queue and record them in the current level
                student = q.popleft()
                current_level.append(str(f"ID: {id} | Name: {name} | Major: {major},"))
    
                #Append student under the left side of the current student to the queue
                if student.left:
                    q.append(root.left)
                #Append student under the right side of the current student to the queue    
                if student.right:
                    q.append(root.right)
                #Each time a student is added to the queue, when they are removed, everything moves back by one
                #and the root position changes to the next student in level-order.
            #Display students with BFS by level on separated lines 
    
                #Counts each level 
        levels += 1
        print(f"Level {levels}: "," ".join(current_level))
#-------------------------------------------------------------------------
#Tree stats:

#Number of students
def count_students(root):
    if root is None:
        return 0
    total_students = 1
    return total_students + count_students(root.left) + count_students(root.right) 

#Smallest ID
def get_min_student(root):
    if root is None:
        return float ('inf')
    left_min = get_min_student(root.left)
    right_min = get_min_student(root.right)

    return min(root.id, left_min, right_min)

#Highest ID
def get_max_student(root):
    if root is None:
        return float ('-inf')
    
    left_max = get_max_student(root.left)
    right_max = get_max_student(root.right)

    return max(root.id, right_max, left_max)

#----------------------------------------------
#Check for integer
def get_int(prompt, low, high):
    while True:
        try:
            x = int(input(prompt))
            if x < low:
                return print("Number is too low")
            if x > high:
                return print("Number is too high")
            return x
        except ValueError:
            return print("Please enter an integer.")
#--------------------------------------------------------------------------------
#Main program 
def main():

    bst = BinarySearchTree()


    done = False
    levels = 0


    #Main Menu:
    while not done:
        print("-----Student Directory----\n")
        print("1. Add new student\n")
        print("2. Search for student by ID \n")
        print("3. Display all students with with DFS\n")
        print("4. Display all students with BFS \n")
        print("5.Display tree stats (total number of students)\n")
        print("6. Display student with the smallest ID and student with the largst ID \n")
        print("7.Exit")

        selected = get_int("Choose an option (1-7): ", 1, 7)

        #--------------------------------------------Add student---------------------------------------
        if selected == 1:
            id = int(input("Enter the student's ID: "))
            name = input("Enter the student's name: ")
            major = input("Enter the student's major: ")

            new_student = student(id, name, major)

            bst.insert(new_student.id,new_student.name,new_student.major)
        #--------------------------------------Find student in directory----------------------------
        if selected == 2:
            target = int(input("Enter the ID of the student you'd like to look for: "))

            print("Visited students: ")
            if (bst.search(new_student,target)):
                print(f"{new_student.name}, student ID {new_student.id}, is a {new_student.major} major")
            else:
                target = int(input("Student not found, please provide another ID: "))
        #--------------------------------------Choose DFS display---------------------------------------
        if selected == 3:
            traversal_choice = input("Would you like to view the student directory in Pre-Order, In-Order, or Post-Order Traversal?")

            if traversal_choice == "Pre-Order":
                bst.preOrderTraversal(student,id)
            if traversal_choice == "In-Order":
                bst.inOrderTraversal(student)
            if traversal_choice == "Post-Order":
                bst.postOrderTraversal(student)
        #-----------------------------------------BFS display----------------------------------------
        if selected == 4:
           bst.bfsTraversal(bst,id,name,major)
        #--------------------------------------------Tree Stats 1 (num of students and tree height)----------------------------
        if selected == 5:
            print(f"Number of students: {count_students(student)}")

            print(f"Tree height: {levels}")
        #----------------------------------------Tree Stats 2 (smallest and largest ID)-----------------------------------
        if selected == 6:
            print(f"Student with smallest ID: {get_min_student(student)}")
            print(f"Student with the largest ID: {get_max_student(student)}")
        #---------------------------------------------EXIT PROGRAM--------------------------
        if selected == 7:
            print("Exiting student directory.")
            done = True
#Call-------------------------------------
main()

        


        










