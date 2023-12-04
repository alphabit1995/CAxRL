# Adding support
        if action == 3:
            print("In action 3: Adding support at position 1")
            if self.support_1_enabled == True:
                print("Support already present at position 1")
                return self.try_next_action()
            self.support_1_enabled = True
            
            if 1 not in self.position_list:
                self.position_list.append(1)

        # Removing support
        if action == 4:
            print("In action 4: Removing support at position 1")
            if self.support_1_enabled == False or len(self.position_list) == 1:
                print("Support already absent at position 1 or only one support present")
                return self.try_next_action()
            self.support_1_enabled = False
            if 1 in self.position_list:
                self.position_list.remove(1)
        ###########################################################################################

        ###########################################################################################
        # Adding support
        if action == 5:
            print("In action 5: Adding support at position 2")
            if self.support_2_enabled == True:
                print("Support already present at position 2")
                return self.try_next_action()
            self.support_2_enabled = True
            if 2 not in self.position_list:
                self.position_list.append(2)

        # Removing support
        if action == 6:
            print("In action 6: Removing support at position 2")
            if self.support_2_enabled == False or len(self.position_list) == 1:
                print("Support already absent at position 2 or only one support present")
                return self.try_next_action()
            self.support_2_enabled = False
            if 2 in self.position_list:
                self.position_list.remove(2)
        ###########################################################################################
        
        ###########################################################################################
        # Adding support
        if action == 7:
            print("In action 7: Adding support at position 3")
            if self.support_3_enabled == True:
                print("Support already present at position 3")
                return self.try_next_action()
            self.support_3_enabled = True
            if 3 not in self.position_list:
                self.position_list.append(3)

        # Removing support
        if action == 8:
            print("In action 8: Removing support at position 3")
            if self.support_3_enabled == False or len(self.position_list) == 1:
                print("Support already absent at position 3 or only one support present")
                return self.try_next_action()
            self.support_3_enabled = False
            if 3 in self.position_list:
                self.position_list.remove(3)
        ###########################################################################################

        ###########################################################################################
        # Adding support
        if action == 9:
            print("In action 9: Adding support at position 4")
            if self.support_4_enabled == True:
                print("Support already present at position 4")
                return self.try_next_action()
            self.support_4_enabled = True
            if 4 not in self.position_list:
                self.position_list.append(4)
        
        # Removing support
        if action == 10:
            print("In action 10: Removing support at position 4")
            if self.support_4_enabled == False or len(self.position_list) == 1:
                print("Support already absent at position 4 or only one support present")
                return self.try_next_action()
            self.support_4_enabled = False
            if 4 in self.position_list:
                self.position_list.remove(4)
        ###########################################################################################

        ###########################################################################################
        # Adding support
        if action == 11:
            print("In action 11: Adding support at position 5")
            if self.support_5_enabled == True:
                print("Support already present at position 5")
                return self.try_next_action()
            self.support_5_enabled = True
            if 5 not in self.position_list:
                self.position_list.append(5)
        
        # Removing support
        if action == 12:
            print("In action 12: Removing support at position 5")
            if self.support_5_enabled == False or len(self.position_list) == 1:
                print("Support already absent at position 5 or only one support present")
                return self.try_next_action()
            self.support_5_enabled = False
            if 5 in self.position_list:
                self.position_list.remove(5)
        ###########################################################################################

        ###########################################################################################
        # Adding support
        if action == 13:
            print("In action 13: Adding support at position 6")
            if self.support_6_enabled == True:
                print("Support already present at position 6")
                return self.try_next_action()
            self.support_6_enabled = True
            if 6 not in self.position_list:
                self.position_list.append(6)
        
        # Removing support
        if action == 14:
            print("In action 14: Removing support at position 6")
            if self.support_6_enabled == False or len(self.position_list) == 1:
                print("Support already absent at position 6 or only one support present")
                return self.try_next_action()
            self.support_6_enabled = False
            if 6 in self.position_list:
                self.position_list.remove(6)
        ###########################################################################################

        ###########################################################################################
        # Adding support
        if action == 15:
            print("In action 15: Adding support at position 7")
            if self.support_7_enabled == True:
                print("Support already present at position 7")
                return self.try_next_action()
            self.support_7_enabled = True
            if 7 not in self.position_list:
                self.position_list.append(7)
        
        # Removing support
        if action == 16:
            print("In action 16: Removing support at position 7")
            if self.support_7_enabled == False or len(self.position_list) == 1:
                print("Support already absent at position 7 or only one support present")
                return self.try_next_action()
            self.support_7_enabled = False
            if 7 in self.position_list:
                self.position_list.remove(7)
        ###########################################################################################

        ###########################################################################################
        # Adding support
        if action == 17:
            print("In action 17: Adding support at position 8")
            if self.support_8_enabled == True:
                print("Support already present at position 8")
                return self.try_next_action()
            self.support_8_enabled = True
            if 8 not in self.position_list:
                self.position_list.append(8)
        
        # Removing support
        if action == 18:
            print("In action 18: Removing support at position 8")
            if self.support_8_enabled == False or len(self.position_list) == 1:
                print("Support already absent at position 8 or only one support present")
                return self.try_next_action()
            self.support_8_enabled = False
            if 8 in self.position_list:
                self.position_list.remove(8)
        ###########################################################################################

        ###########################################################################################
        # Adding support
        if action == 19:
            print("In action 19: Adding support at position 9")
            if self.support_9_enabled == True:
                print("Support already present at position 9")
                return self.try_next_action()
            self.support_9_enabled = True
            if 9 not in self.position_list:
                self.position_list.append(9)
        
        # Removing support
        if action == 20:
            print("In action 20: Removing support at position 9")
            if self.support_9_enabled == False or len(self.position_list) == 1:
                print("Support already absent at position 9 or only one support present")
                return self.try_next_action()
            self.support_9_enabled = False
            if 9 in self.position_list:
                self.position_list.remove(9)
        ###########################################################################################

        ###########################################################################################
        # Adding support
        if action == 21:
            print("In action 21: Adding support at position 10")
            if self.support_10_enabled == True:
                print("Support already present at position 10")
                return self.try_next_action()
            self.support_10_enabled = True
            if 10 not in self.position_list:
                self.position_list.append(10)
        
        # Removing support
        if action == 22:
            print("In action 22: Removing support at position 10")
            if self.support_10_enabled == False or len(self.position_list) == 1:
                print("Support already absent at position 10 or only one support present")
                return self.try_next_action()
            self.support_10_enabled = False
            if 10 in self.position_list:
                self.position_list.remove(10)
        ###########################################################################################

        ###########################################################################################
        # Adding support
        if action == 23:
            print("In action 23: Adding support at position 11")
            if self.support_11_enabled == True:
                print("Support already present at position 11")
                return self.try_next_action()
            self.support_11_enabled = True
            if 11 not in self.position_list:
                self.position_list.append(11)
        
        # Removing support
        if action == 24:
            print("In action 24: Removing support at position 11")
            if self.support_11_enabled == False or len(self.position_list) == 1:
                print("Support already absent at position 11 or only one support present")
                return self.try_next_action()
            self.support_11_enabled = False
            if 11 in self.position_list:
                self.position_list.remove(11)
        ###########################################################################################

        ###########################################################################################
        # Adding support
        if action == 25:
            print("In action 25: Adding support at position 12")
            if self.support_12_enabled == True:
                print("Support already present at position 12")
                return self.try_next_action()
            self.support_12_enabled = True
            if 12 not in self.position_list:
                self.position_list.append(12)
        
        # Removing support
        if action == 26:
            print("In action 26: Removing support at position 12")
            if self.support_12_enabled == False or len(self.position_list) == 1:
                print("Support already absent at position 12 or only one support present")
                return self.try_next_action()
            self.support_12_enabled = False
            if 12 in self.position_list:
                self.position_list.remove(12)
        ###########################################################################################

        ###########################################################################################
        # Adding support
        if action == 27:
            print("In action 27: Adding support at position 13")
            if self.support_13_enabled == True:
                print("Support already present at position 13")
                return self.try_next_action()
            self.support_13_enabled = True
            if 13 not in self.position_list:
                self.position_list.append(13)
        
        # Removing support
        if action == 28:
            print("In action 28: Removing support at position 13")
            if self.support_13_enabled == False or len(self.position_list) == 1:
                print("Support already absent at position 13 or only one support present")
                return self.try_next_action()
            self.support_13_enabled = False
            if 13 in self.position_list:
                self.position_list.remove(13)
        ###########################################################################################
