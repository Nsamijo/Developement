class Program {
  public static void Main() {
    int[] arr = new int[]{list};
    int n = 5;
    int count = 0;
    foreach(var i in arr){
      if(i > n){
        count++;
      }
    }
    string s = "There are " + count + " values that are greater than " + n;
  }
}