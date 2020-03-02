class Program {
  public static void Main() {
    int len = 10;
    var arr = new int[len];
   
    for(int i = 0; i < len; i++)
    {
      if(i == 0){
        arr[0] = 0;
      }else if(i == 1){
        arr[1] = 1;
      }else{
        arr[i] = arr[i - 1] + arr[i - 2];
      }
    }
    string s = "fib(" + (len - 1) + ") = " + arr[len - 1];
  }
}