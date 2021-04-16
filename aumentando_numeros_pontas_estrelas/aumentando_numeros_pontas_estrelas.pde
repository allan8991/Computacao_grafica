
 float k=0;
 void setup(){
  size (500,500);  
}

void draw()
{    
  background(220);
  fill(0,0,255);
  rect(0,0,width,height);
  int margem=20;
  int margem1=180;
  float n= round(map(mouseY,0,width,3,12));
  float a = TWO_PI/n;
  float r=(width/2)-margem;
  float r1=(width/2)-margem1;
  translate(width/2,height/2);  
  rotate( (TWO_PI/5)+k);
  fill(255,255,0);
  stroke(255,255,0); 
  beginShape();
  for(int i=0;i<2*n;i++)
  {
    float x,x1;
    float y,y1; 
      if(i%2==0){    
         x=r*cos(i*a/2);
         y=r*sin(i*a/2);
         vertex(x,y);
     }else{       
       x1=r1*cos(i*a/2);
       y1=r1*sin(i*a/2);   
       vertex(x1,y1);
       
     }  
 }
  endShape(CLOSE);
  k+=0.009;
}

  
