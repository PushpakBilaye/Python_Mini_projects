#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("****************************************")
print("***************#  MENU  #***************")
print("****************************************")
print(" 1. STRING \n 2. LIST \n 3. TUPLE \n 4. SET \n 5. DICTIONARY \n 0. EXIT")
ch=int(input("Enter a number to select following datatype: "))
print("****************************************")
while(True):
    while(True):
#STRING
        if ch==1:
            print(" 1. Definition and syntax \n 2. INDEXING and SLICING \n 3. Length of string \n 4. Concatinate two strings \n 0. Exit")
            string1=int(input("Enter an option from above: "))
            if string1==1:
                print("i. String is a collection of different characters i.e. numbers,symbols,letters.")
                print("ii. We can define string using Single quotes- (' '), Double quotes- (""), triple quotes- ("'string'") ")
                print(" Syntax: \n variable_name='(String)' ")
                print(" Example: \n string='python' \n")
                continue
    #index_slice_str
            elif string1==2:
                print("\nIndexing-To get a single character of string. \nSlicing-To get multiple characters of string.")
                print("1. Indexing \n2. Slicing")
                str2=int(input("Choose correct option from above to display execution of string: "))
                if str2==1:
                    s1=input("Enter a string: ")
                    si1=int(input("Enter index of string: "))
                    s_result1=s1[si1]
                    print(s_result1)
                elif str2==2:
                    s2=input("Enter a string: ")
                    start=int(input("Enter starting index of string: "))
                    end=int(input("Enter ending index of string: "))
                    step=int(input("Enter stepping in index of string: "))
                    s_result2=s2[start:end:step]
                    print(s_result2)
                else:
                    print("INVALID INPUT!!")
                    continue
                continue
    #len_str
            elif string1==3:
                str3=input("Enter a string to get length of it: ")
                s_result3=len(str3)
                print("Length of string is",s_result3)
                continue
    #concate_str
            elif string1==4:
                print("\nConcatination has two types i.e. using + and * operators.")
                print("+ operator combines two or more strings.\n* operator multiplies given string by given number of times.")
                print("1. Using + \n2. Using *")
                str4=int(input("Select a number from above options: "))
                if str4==1:
                    str4_1=input("Enter first string: ")
                    str4_2=input("Enter second string: ")
                    s_result41= str4_1 + str4_2
                    print("Concatinated string is:",s_result41)
                elif str4==2:
                    str4_3=input("Enter a string: ")
                    str4_4=int(input("How many times you want to display above string: "))
                    s_result42= str4_3 * str4_4
                    print("Concatinated string is:",s_result42)
                else:
                    print("INVALID INPUT!!")
                continue
    #exit_str
            elif string1==0:
                print("!!! THANK YOU !!!")
                break

            else:
                print("**************INVALID INPUT!!************** \nPLEASE CHOOSE CORRECT OPTION!!\n")
                continue

    #LIST
        elif ch==2:
            print(" 1. Definition and Syntax\n 2. Indexing and Slicing\n 3. Append\n 4. Insert\n 5. Extend\n 6. Pop\n 7. Remove\n 8. Clear\n 9. Delete\n 0. Exit")
            list1=int(input("Select an option from above: "))
            if list1==1:
                print("i. Lists are ordered collection of heterogenous elements which are mutable.\nii. Heterogenous means it can have strings, numbers etc.")
                print("iii. We can change the original list dynamically hence they are mutable in nature.\niv. We can define empty list using [] square brackets or keyword-function list().\nv. We can perform indexing and slicing on lists because they are ordered collection of elements.")
                print("\nSyntax:\n List_name=[element1,element2,....,elementn]")
                print("\nExample:\n L1=[1,2,3,'n1','n2']")
                continue
    #index_slice_list        
            elif list1==2:
                print("\nIndexing-To get a single element of list. \nSlicing-To get multiple elements of list.")
                print("1. Indexing \n2. Slicing")
                lst2=int(input("Choose correct option from above to display execution of list: "))
                if lst2==1:
                    l1=list(input("Enter elements in a list: ").split())           #Split() for separating elements with spaces
                    li1=int(input("Enter index of list: "))
                    print(l1[li1])
                elif lst2==2:
                    l2=list(input("Enter elements in a list: ").split())
                    start=int(input("Enter starting index of list: "))
                    end=int(input("Enter ending index of list: "))
                    step=int(input("Enter stepping in index of list: "))
                    print(l2[start:end:step])
                else:
                    print("INVALID INPUT!!")
                continue
    #append_list     
            elif list1==3:
                print("\nAppend function adds an element in the original list at the end.")
                lst3=list(input("Enter elements in a list: ").split())
                l1=list(input("Enter an element that you have to append: ").split())
                lst3.append(l1)
                print(lst3)
                continue
    #insert_list
            elif list1==4:
                print("\nInsert function adds an element in the original list at specific position.")
                lst4=list(input("Enter elements in a list: ").split())
                l1=list(input("Enter an element that you have to insert: ").split())
                lpos=int(input("Write a specific index from original list where you have to insert above input: "))
                lst4.insert(lpos,l1)
                print(lst4)
                continue
    #extend_list         
            elif list1==5:
                print("\nExtend function adds multiple elements in the original list at the end.")
                lst5=list(input("Enter elements in a list: ").split())
                l1=list(input("Enter multiple elements that you have to extend: ").split())
                lst5.extend(l1)
                print(lst5)
                continue
    #pop_list    
            elif list1==6:
                print("\nPop function removes last element by default, but we can remove it by indexing.")
                lst6=list(input("Enter elements in a list: ").split())
                lpos=int(input("Write a specific index position from original list where you have to pop above input: "))
                lst6.pop(lpos)
                print(lst6)
                continue
    #remove_list         
            elif list1==7: 
                print("\nRemove function removes an element by value of element.")
                lst7=list(input("Enter elements in a list: ").split())
                lval=input("Write a specific value element from original list where you have to remove above input: ")
                lst7.remove(lval)
                print(lst7)
                continue
    #clear_list  
            elif list1==8:
                print("\nClear function clears all elements from the list except its structure.")
                lst8=list(input("Enter elements in a list: ").split())
                lst8.clear()
                print(lst8)
                continue
    #del_list           
            elif list1==9:
                print("\ndel keyword deletes the whole list with structure.")
                lst8=list(input("Enter elements in a list: ").split())
                del lst8
                print("NameError: name is not defined")
                continue
    #exit_list            
            elif list1==0:
                print("!!! THANK YOU !!!")
                break

            else:
                print("**************INVALID INPUT!!************** \nPLEASE CHOOSE CORRECT OPTION!!\n")
                continue

    #TUPLE 
        elif ch==3:
            print(" 1. Definition and Syntax\n 2. Indexing and Slicing\n 3. Length of given tuple\n 4. Delete\n 0. Exit")
            tuple1=int(input("Enter an option from above: "))
            if tuple1==1:
                print("i. Tuples are Ordered collection of heterogenous elements which are immutable.\nii. Tuples are faster than Lists w.r.t. iterations.")
                print("iii. Tuples can be defined by round brackets () or keyword-function tuple().")
                print("Syntax:\ntuple_name=(element1, element2,...,elementn) \nExample: \nt1=(1,2,3,'n1')")
                continue
    #index_slice_tuple            
            elif tuple1==2:
                print("\nIndexing-To get a single element of tuple. \nSlicing-To get multiple elements of tuple.")
                print("1. Indexing \n2. Slicing")
                tpl2=int(input("Choose correct option from above to display execution of tuple: "))
                if tpl2==1:
                    t1=tuple(input("Enter elemets of a tuple: ").split())
                    ti1=int(input("Enter index of tuple: "))
                    t_result1=t1[ti1]
                    print(t_result1)
                elif tpl2==2:
                    t2=tuple(input("Enter elements of a tuple: ").split())
                    start=int(input("Enter starting index of tuple: "))
                    end=int(input("Enter ending index of tuple: "))
                    step=int(input("Enter stepping in index of tuple: "))
                    t_result2=t2[start:end:step]
                    print(t_result2)
                else:
                    print("INVALID INPUT!!")
                    continue
                continue
    #len_tuple            
            elif tuple1==3:
                tpl3=tuple(input("Enter a tuple to get length of it: ").split())
                t_result3=len(tpl3)
                print("Length of tuple is",t_result3)
                continue
    #del_tuple            
            elif tuple1==4:
                print("del keyword deletes the whole tuple with structure.")
                tpl4=tuple(input("Enter elements in a tuple: ").split())
                del tpl4
                print("NameError: name is not defined")
                continue
    #exit_tuple            
            elif tuple1==0:
                print("!!! THANK YOU !!!")
                break

            else:
                print("**************INVALID INPUT!!************** \nPLEASE CHOOSE CORRECT OPTION!!\n")
                continue

    #SET
        elif ch==4:
            print(" 1. Definition and Syntax\n 2. Add\n 3. Update\n 4. Pop\n 5. Remove\n 6. Discard\n 7. Clear\n 8. Delete\n 9. Mathematical Operations\n 0. Exit")
            set1=int(input("Enter an option from above: "))
            if set1==1:
                print("i. SET are unordered collections of heterogenous elements which are mutable. \nii. We can define sets by keyword function set().")
                print("iii. Set does not accept duplicate elements. \niv. The elements of sets are aligned randomly hence they are unordered.")
                print("Syntax: \nset_name={element1,element2,...,elementn}")
                print("Example: \ns1={1,2,3,4,'ss','se'}")
                continue
    #add_set            
            elif set1==2:
                print("We uses add() function to add single element.")
                st2=set(input("Enter set of elements: ").split())
                s1=input("Enter an element to add: ")
                st2.add(s1)
                print(st2)
                continue
    #update_set            
            elif set1==3:
                print("Update function updates or add multiple elements.")
                st3=set(input("Enter set of elements: ").split())
                s2=input("Enter number of elements to update: ").split()
                st3.update(s2)
                print(st3)
                continue
    #pop_set            
            elif set1==4:
                print("Pop function deletes an element.")
                st4=set(input("Enter set of elements: ").split())
                st4.pop()
                print(st4)
                continue
    #remove_set            
            elif set1==5:
                print("Remove function removes an element by value of that element.")
                st5=set(input("Enter set of elements: ").split())
                s5=input("Write a specific value element from original set where you have to remove above input: ")
                st5.remove(s5)
                print(st5)
                continue
    #discard_set            
            elif set1==6:
                print("Discard method is used when we have to remove an element from set. But if that element is not present in that set then it will not give an error.")
                st6=set(input("Enter set of elements: ").split())
                s6=input("Write a specific value element from original set where you have to discard above input: ")
                st6.discard(s6)
                print(st6)
                continue
    #clear_set            
            elif set1==7:
                print("Clear function clears all elements from the set except its structure.")
                st7=set(input("Enter set of elements: ").split())
                st7.clear()
                print(st7)
                continue
    #del_set            
            elif set1==8:
                print("del keyword deletes the whole set with structure.")
                st8=set(input("Enter elements in a set: ").split())
                del st8
                print("NameError: name is not defined")
                continue
    #mathematical_operations_set            
            elif set1==9:
                print("1. Union \n2. Intersection \n3. Difference \n4. Symmetric-Difference")
                st9=int(input("Enter an option from above: "))
                if st9==1:
                    print("\nUnion combines two sets.")
                    s1=set(input("Enter first set of elements: ").split())
                    s2=set(input("Enter second set of elements: ").split())
                    print(s1|s2)
                elif st9==2:
                    print("\nIntersection displays common elements.")
                    s1=set(input("Enter first set of elements: ").split())
                    s2=set(input("Enter second set of elements: ").split())
                    print(s1&s2)
                elif st9==3:
                    print("\nDifference displays unmatched elements from first set.")
                    s1=set(input("Enter first set of elements: ").split())
                    s2=set(input("Enter second set of elements: ").split())
                    print(s1-s2)
                elif st9==4:
                    print("\nSymmetric-Difference is used to show unmatched elements from both sets.")
                    s1=set(input("Enter first set of elements: ").split())
                    s2=set(input("Enter second set of elements: ").split())
                    print(s1^s2)
                else:
                    print("INVALID INPUT!!")
                    continue
                continue
    #exit_set            
            elif set1==0:
                print("!!! THANK YOU !!!")
                break

            else:
                print("**************INVALID INPUT!!************** \nPLEASE CHOOSE CORRECT OPTION!!\n")
                continue

    #DICTIONARY
        elif ch==5:
            print(" 1. Definition and Syntax\n 2. Add\n 3. Update\n 4. Clear\n 5. Delete\n 0. Exit ")
            dict1=int(input("Enter an option from above: "))
            if dict1==1:
                print("i. Dictionary is a collection of key-value pair. \nii. Dictionaries are unordered i.e. we can not perform indexing and slicing.")
                print("iii. Dictionaries are Heterogenous and mutable in nature. \niv. we can define dictionaries by curly brackets {} or dict() keyword-function.")
                print("Syntax: \ndict_name={key1:value1, key2:value2,...,keyn:valuen}")
                print("Example: \nd1={'a':11, 'b1':'s',1:3}")
                continue
    #add_a_dict            
            elif dict1==2:
                print("We can add single element of key value pair in existing dictionary.")
                d1={"abc":123, "efg":456, "hij":789}
                print("Dictionary before adding a single element: d1= ",d1)
                print("d1['klm']=101112")
                d1['klm']=101112
                print("Dictionary after adding single element: ",d1)
                continue
    #update_dict        
            elif dict1==3:
                print("Update method updates or adds multiple key value pairs in dictionary.")
                d2={"abc":123, "efg":456, "hij":789}
                print("Dictionary before updation: d2= ",d2)
                print("d2.update({'klm':101112, 'nop':131415})")
                d2.update({'klm':101112, 'nop':131415})
                print("Dictionary after updation: ",d2)
                continue
    #clear_dict            
            elif dict1==4:
                print("Clear function is used to remove all elements of dictionary without structure.")
                d4={"abc":123, "efg":456, "hij":789}
                print("Dictionary before updation: d4= ",d4)
                print("d4.clear()")
                d4.clear()
                print("Output: ",d4)
                continue
    #del_dict        
            elif dict1==5:
                print("del function deletes whole dictionary including structure of it.")
                d5={"abc":123, "efg":456, "hij":789}
                print("Dictionary before updation: d5= ",d5)
                print("del d5")
                del d5
                print("NameError: name is not defined")
                continue 
    #exit_dict            
            elif dict1==0:
                print("!!! THANK YOU !!!")
                break

            else:
                print("**************INVALID INPUT!!************** \nPLEASE CHOOSE CORRECT OPTION!!\n")
                continue
    #EXIT        
        else:
            print("!!! Thank You !!!")
            break
        break
    break


# In[ ]:




