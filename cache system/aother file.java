import org.apache.jcs.JCS;  
public class StuObjManager {  
    private static StuObjManager instance;  
    private static int checkedOut=0;  
    public static JCS stuCache;  
    private StuObjManager()  
    {  
        try  
        {  
            stuCache=JCS.getInstance("stuCache");  
        }  
        catch(Exception e)  
        {  
            e.printStackTrace();  
        }  
    }  
      
    public static StuObjManager getInstance()  
    {  
        synchronized(StuObjManager.class)  
        {  
            if(instance==null)  
            {  
                instance=new StuObjManager();  
            }  
              
        }  
        synchronized(instance)  
        {  
            instance.checkedOut++;  
        }  
        return instance;  
    }  
      
    public Student getStu(int sno)  
    {  
      return getStu(sno,true);    
    }  
    public Student getStu(int sno,boolean a)  
    {  
        Student stu=null;  
        if(a)  
        {  
            stu=(Student)stuCache.get("Stu"+sno);  
        }  
        if(stu==null)  
        {  
              stu=loadStu(sno);  
        }  
        return stu;  
    }  
    public Student loadStu(int sno)  
    {  
        Student stu=new Student();  
        stu.sno=sno;  
        try  
        {  
            boolean found=false;  
            found=true;  
            if(found)  
            {  
                stuCache.put("Stu"+sno, stu);  
            }  
        }  
        catch(Exception e)  
        {System.out.println("ERROR!");}  
        return stu;  
    }  
      
    public void storeStu(Student stu)  
    {  
        try  
        {  
            if(stu.sno!=0)  
            {  
                stuCache.remove("Stu"+stu.sno);  
            }  
            stuCache.put("Stu"+stu.sno, stu);  
        }  
        catch(Exception e)  
        {}  
    }  
    public static void main(String [] args)  
    {  
        long last=System.currentTimeMillis();  
        StuObjManager stu=StuObjManager.getInstance();  
        for(int i = 0; i < 2000; i++){  
            stu.loadStu(i);  
        }  
        Student stu1=stu.getStu(8,true);  
        System.out.println(stu1.sno);  
        System.out.println("time:"+(System.currentTimeMillis()-last));  
    }  
}  