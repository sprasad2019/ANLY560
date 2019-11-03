Main.java
import java.sql.*;

public class Main

    public static void main(String[] args)
        Record record = new Record(John, Doe, 10);

        createTable();
        insertRecord(record);
   
    public static Connection createTable()
        Connection connection = null;
        Statement stmt = null;

        try
            connection = getConnection();
            connection.setAutoCommit(false);

            stmt = connection.createStatement();
            String sql = CREATE table TABLE (FirstName char(50), LastName char(50, Age int(3));;
            stmt.executeUpdate(sql);
            connection.commit();
            connection.close();
            connection = null;
       
        return connection;

    public static Connection insertRecord(Record)
        Connection connection = null;
        Statement stmt = null;

        try
            connection = getConnection();
            connection.setAutoCommit(false);

            stmt = connection.createStatement();
            String sql = INSERT into TABLE values Record ;;
            stmt.executeUpdate(sql);
            connection.commit();
            connection.close();

            System.out.println((Inserted Record + Record + ) done successfully);
        catch ( Exception e )
            System.out.println(e);
            connection = null;
       
        return connection;


   