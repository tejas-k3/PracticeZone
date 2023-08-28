// n : Number of plates
// Origin: 1st tower, Buffer: Tower that will be used as buffer , Destination: Tower on which all plates has to transferred.
void moveTowers(int n, Tower destination, Tower buffer) {
       if(n>0) {
	      moveTowers(n-1, buffer, destination);
		  moveTopElement(destination);
		  moveTowers(n-1, destination, origin);
	   }
}
// This is a method in Tower class
 void moveTopTo(Tower t) { 
         int top= disks.pop(); 
         t.add(top);
 }