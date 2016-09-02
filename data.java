package datasets;


import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;

public class data {

	public static void main(String args[]) throws IOException{
		
		String csvFile = "C:/Users/Siddesh/Desktop/Big Data F/final.csv";
		File f=new File("output.csv");
		BufferedReader br = null;
		String line = "";
		String cvsSplitBy = ",";
		String Y;
		String put_data_dep = "0";
		String put_data_arr = "0";
		String put_data_est = "0";
		br = new BufferedReader(new FileReader(csvFile));
		PrintWriter out = new PrintWriter(f);
		while ((line = br.readLine()) != null) {
		
			String[] data = line.split(cvsSplitBy);
			String departure = data[4];
			String actual_arrival = data[6];
			String estimated_arrival = data[7];
			
			
			String orig_dep[] = departure.split("\\s+");
			String orig_arr[] = actual_arrival.split("\\s+");
			String est_arr[] = estimated_arrival.split("\\s+");
			
		
			for (int i = 0 ; i < orig_dep.length; i++){
				if(i == 1){
					put_data_dep = orig_dep[1];
					put_data_arr = orig_arr[1];
					put_data_est = est_arr[1];
				}
			}
			
			
			if( put_data_arr.compareTo(put_data_est) < 0){
				Y = "1";
			}
			else{
				Y = "0";
			}
			
			String temp_dep = "  ";
			String temp_arr = "  ";
			
			System.out.println(put_data_dep);
			System.out.println(put_data_arr);
			
			String abc[] = null;
			String bbc[] = null;
			
			if(put_data_dep.length() > 0 ){
				abc = put_data_dep.split(":");
				bbc = put_data_arr.split(":");
				
			}
			System.out.println(abc[0]);
			System.out.println(bbc[0]);

			int a = Integer.parseInt(abc[0]);
			int b = Integer.parseInt(bbc[0]);
			out.println(a+","+b+","+Y+",");
		}
		out.close();
	}
}
