package sakila;

// Import required pacakges
import java.sql.*;

public class Data {
   // Provide JDBC driver name and database URL
   static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
   static final String DB_URL = "jdbc:mysql://localhost/sakila";

   //  Provide database login credentials
   static final String USER = "root";
   static final String PASS = "";
   
   public static void main(String[] args) {
   Connection conn = null;
   Statement stmt = null;
   try{
      Class.forName("com.mysql.jdbc.Driver");

   //Connect to database
      System.out.println("Connecting to database...");
      conn = DriverManager.getConnection(DB_URL,USER,PASS);


// Execute a query
      System.out.println("Creating statement...");
      stmt = conn.createStatement();
      String sql;
      sql = "SELECT actor_id, first_name, last_name FROM actor";
      ResultSet rs = stmt.executeQuery(sql);

      // Extract data from result set
      while(rs.next()){
         //Retrieve by column name
         int actor_id  = rs.getInt("actor_id");
         String firstname = rs.getString("first_name");
         String lastname = rs.getString("last_name");

         //Display values
         System.out.print("ActorID: " + actor_id);
         System.out.print(", First name: " + firstname);
         System.out.println(", Last name: " + lastname);
      }

      rs.close();
      stmt.close();
      conn.close();
   }catch(SQLException se){
      se.printStackTrace();
   }catch(Exception e){
      e.printStackTrace();
   }finally{
      try{
         if(stmt!=null)
            stmt.close();
      }catch(SQLException se2){
      }
      try{
         if(conn!=null)
            conn.close();
      }catch(SQLException se){
         se.printStackTrace();
      }
   }//end try
}//end main
}
