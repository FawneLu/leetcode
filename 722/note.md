###每一个条件都进行判断算了
这个遍历的方式是加入multi变量是不是一个多行的注释。根据这个变量进行针对性的操作。如果不是多行注释，遇到//直接跳过，遇到/*要把multi改成多行标记并把i+1来跳过*号，如果不是上述两种注释则为正常的代码，加入字符串变量。如果是多行注释时，遇到*/修改multi结束多行字符串并把i+1来跳过/号。