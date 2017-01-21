import java.io.Serializable;  
import java.util.List;  
public class Student implements Serializable{  
    /** 
     *  
     */  
    public static final long serialVersionUID = 1L;  
    public int sno;  
    public String sname;  
      
      
    public Student()  
    {}  
    public int getSno(){  
     return this.sno;  
    }  
    public void setSno(int no){  
     this.sno=no;  
    }  
    public String getSname(){  
     return this.sname;  
    }  
    public void setSname(String name){  
     this.sname=name;  
    }  
}  