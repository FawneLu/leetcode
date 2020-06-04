### 类似于merge intervals
比merge interval还要简单。就每一个interval跟新的的start和end比较。  如果interval的end比start小，不用管，同理，interval的start比end大不用管。 否则，start变为两个start里小的那个，end变为两个end里大的那个。