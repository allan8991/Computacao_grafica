
float p2x=450;
  float p2y=100;
  float p3x=450;
  float p3y=500;
  float p4x=700;
  float p4y=80;  

void setup(){
  size (950,910);  
}
void draw(){
  background(200);
  float p1x=mouseX;
  float p1y=mouseY;
  noFill();
     stroke(255,0,0);
  beginShape();
  for(float t=0;t<=1;t+=0.04){
    float fx=p1x+t*(p2x-p1x);
    float fy=p1y+t*(p2y-p1y);
    float gx=p2x + t*(p3x-p2x);
    float gy=p2y + t*(p3y-p2y);
    float hx= p3x+ t*(p4x-p3x);
    float hy= p3y+ t*(p4y-p3y);
    float jx = fx+t*(p4x-p3x);
    float jy= fy+t*(gy-fy);
    float lx=gx+t*(hx-gx);
    float ly=gy+t*(hy-gy);
    float mx=jx+t*(lx-jx);
     float my=jy+t*(ly-jy);  
    
    vertex(mx,my);
  
  }
  
  endShape();
   stroke(80,80,80);
  fill(80,80,80);
  circle(p1x,p1y,8);
  circle(p2x,p2y,8);
  circle(p3x,p3y,8);
  circle(p4x,p4y,8);
}  
  
