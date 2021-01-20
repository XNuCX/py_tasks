def input_layer():
    n, m = [int(el) for el in input().split(" ")]
    layer_1 = []
    bricks = []
    for _ in range(n):
        line = [int(el) for el in input().split(" ")]
        """creating list with the input line"""
        bricks.append(max(line))
        """taking the max number from each line and adding it to
        a list with the possible number of bricks"""
        layer_1.append(line)
    number_of_bricks = max(bricks)

    return [n, m, layer_1, number_of_bricks]


class Layer:
    """Reusable class for creating multiple Layer objects"""
    def __init__(self, n, m, layer_1, bricks):
        self.line = n
        self.column = m
        self.layer_initial = [str(el) for el in layer_1]
        self.layer = [[False for _ in range(self.column + 1)] for _ in range(len(self.line) + 1)]
        self.blocks = bricks
        self.count = 0
        self.flag_end = False
        self.flag_match = False
        self.block_full_size = {}
        self.database = [{str(el): {"times_overlay": 0, "times_occurrence": 0}} for el in range(1, self.blocks + 1)]

    def sorting_value_name(self, name, val):
        first_with_val_zero = []
        # first_with_val_zero = [el for el in self.database if el.values()["times_overlay"] == val]
        for database_el in self.database:
            for el_value in database_el.values():
                if el_value[name] == val:
                    first_with_val_zero.append(database_el)
        if not first_with_val_zero:
            return False
        return first_with_val_zero

    def sorting_name(self):
        pass


    def iterating(self):
        """Iterating in the initial layer"""
        for l_0, line in enumerate(self.layer):
            for c_0, column in enumerate(line):
                self.checking()

    def checking(self):

        """Checking if the rules matched"""
        key = ''
        index = int
        counter = 1
        for l_0, line in enumerate(self.layer):

            for c_0, column in enumerate(line):
                if l_0 % 2 == 0:
                    while True:
                        if not column:
                            if not self.count == 2:
                                if not self.count == 1:
                                    key = self.sorting_value_name("times_overlay", 0)[0].keys()
                                    if not key:
                                        break
                                    key = str(key)
                                for i, el in enumerate(self.database):
                                    if el.keys() == key:
                                        index = i

                                self.layer[l_0][c_0] = key
                                if self.layer[l_0][c_0] == self.layer_initial[l_0][c_0]:
                                    # key = self.layer[l_0][c_0]
                                    # for el in self.database:
                                    #     if el.keys() == key:
                                    #         el[key]["times_overlay"] += 1
                            
                                    self.database[index][key]["times_overlay"] += 1
                                    if self.database[index][key]["times_overlay"] == 2:
                                        self.layer[l_0][c_0] = False
                                        self.database[index][key]["times_overlay"] -= 1
                                        self.count = 0
                                        continue
                                    else:
                                        self.database[index][key]["times_occurrence"] += 1
                                else:
                                    # self.layer[l_0][c_0] = key
                                    self.database[index][key]["times_occurrence"] += 1
                        
                                self.count += 1
                                break
                            else:
                                self.count = 0

                else:
                    data_keys_1_occ = self.sorting_value_name("times_occurrence", 1)[:]

                    for t, k in enumerate(data_keys_1_occ):
                        key_dat_k = k.keys()
                        for i, el in enumerate(self.database):
                            if el.keys() == key_dat_k:
                                index = i

                        if key_dat_k == self.layer[l_0 - 1][c_0]:
                            self.layer[l_0][c_0] = key_dat_k
                            self.database[index][key]["times_occurrence"] += 1
                            if self.layer[l_0][c_0] ==\
                                    self.layer_initial[l_0][c_0]\
                                    and self.database[index][key_dat_k]["times_overlay"] == 2:
                                self.layer[l_0][c_0] = False
                                self.layer[l_0 - 1][c_0] = False
                                self.database[index][key_dat_k]["times_occurrence"] = 0
                                self.database[index][key_dat_k]["times_overlay"] = 0




            




















        # for block_number in range (1, self.blocks + 1):
        #     self.count += 1
        #     if not self.layer:
        #         """If the layer is empty try to return the unused
        #         block number for starting a fresh new variation
        #         of the layer"""
        #         if block_number < self.count:
        #             """Check if the block is already been processed
        #             if "Yes" - skipping this block try the next one"""
        #             if block_number == self.blocks: self.flag_end = True
        #             """checking if this was the last possible variation of the Layer"""
        #             continue
        #         else:
        #             if block_number == self.layer_initial[line][column]:
        #                 self.block_full_size[block_number] = 1
        #             return block_number
        #     else:
        #
        #         if len(list(el.count(block_number) for el in self.layer)) >= 2:
        #             continue
        #         elif self.layer[line][column] == self.layer_initial[line][column]:
        #             if self.block_full_size[block_number]:
        #                 self.block_full_size[block_number] += 1
        #             else:
        #                 self.block_full_size[block_number] = 1
        #             if self.block_full_size[block_number] == 2:


    def inserting(self):
        """Creating the new Layer"""
        for i in range(self.line):

            for n in range(self.column):
                # self.layer[i].append(self.checking(i, n))
                self.count = 1



print(*input_layer())
layer_2 = Layer(input_layer()).checking()
print(layer_2)