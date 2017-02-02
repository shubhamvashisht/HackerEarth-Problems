import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    
    public static int bbSearch(int[] a, int l, int r, int k) {
        
        if (l <= r) {
            
            int mid = (l + r +1)/2;
            
            if(l==r && k <= a[mid]) {
                
                return mid;
            }
        
            if( mid >= 1 && k > a[mid-1] && k <= a[mid])
                return mid;
        
            if(a[mid] > k)
                return bbSearch(a, l, mid-1, k);
            if(a[mid] < k) 
                return bbSearch(a, mid+1, r, k);
        }
        return -1;    
    }

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int[] a = new int[n];
		int[] pa = new int[n];
		for(int i = 0; i<n; i++) {
			a[i] = in.nextInt();
			if(i == 0)
				pa[i] = a[i];
                        else	
				pa[i] = pa[i-1] + a[i];
		}
        
        int q = in.nextInt();
        for(int i =0; i < q; i++) {
            int idx = in.nextInt();
            int ans = bbSearch(pa, 0, n-1, idx);
            System.out.println(ans + 1);
        }
		

	}
}