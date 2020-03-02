class Program {
  public static void Main() {
    int[] numbers = new int[] {1};
    int temp = 0;
    for (int i = 0, j = numbers.Length - 1; i < numbers.Length / 2; i++, j--) {
      temp = numbers[i];
      numbers[i] = numbers[j];
      numbers[j] = temp;
    }
  }
}