#   " " "  
 #   4 . 6   W r i t e   a   p r o g r a m   t o   p r o m p t   t h e   u s e r   f o r   h o u r s   a n d   r a t e   p e r   h o u r   u s i n g  
 #   r a w _ i n p u t   t o   c o m p u t e   g r o s s   p a y .   A w a r d   t i m e - a n d - a - h a l f   f o r   t h e   h o u r l y   r a t e   f o r  
 #   a l l   h o u r s   w o r k e d   a b o v e   4 0   h o u r s .   P u t   t h e   l o g i c   t o   d o   t h e   c o m p u t a t i o n   o f  
 #   t i m e - a n d - a - h a l f   i n   a   f u n c t i o n   c a l l e d   c o m p u t e p a y ( )   a n d   u s e   t h e   f u n c t i o n   t o   d o   t h e  
 #   c o m p u t a t i o n .   T h e   f u n c t i o n   s h o u l d   r e t u r n   a   v a l u e .   U s e   4 5   h o u r s   a n d   a   r a t e   o f   1 0 . 5 0  
 #   p e r   h o u r   t o   t e s t   t h e   p r o g r a m   ( t h e   p a y   s h o u l d   b e   4 9 8 . 7 5 ) .   Y o u   s h o u l d   u s e   r a w _ i n p u t  
 #   t o   r e a d   a   s t r i n g   a n d   f l o a t ( )   t o   c o n v e r t   t h e   s t r i n g   t o   a   n u m b e r .   D o   n o t   w o r r y   a b o u t  
 #   e r r o r   c h e c k i n g   t h e   u s e r   i n p u t   u n l e s s   y o u   w a n t   t o   -   y o u   c a n   a s s u m e   t h e   u s e r   t y p e s  
 #   n u m b e r s   p r o p e r l y .  
 #   " " "  
  
 # o u t p u t :  
 # 4 9 8 . 7 5  
  
  
 d e f   c o m p u t e p a y ( h , r ) :  
         i f   h   <   0   o r   r   <   0 :  
                 r e t u r n   N o n e  
         e l i f   h   >   4 0 :  
                 r e t u r n   ( 4 0 * r + ( h - 4 0 ) * 1 . 5 * r )  
         e l s e :  
                 r e t u r n   ( h * r )  
  
 t r y :  
         h r s   =   r a w _ i n p u t ( " E n t e r   H o u r s : " )  
         h o u r   =   f l o a t ( h r s )  
         r   =   r a w _ i n p u t ( " p l e a s e   i n p u t   y o u r   r a t e : " )  
         r a t e   =   f l o a t ( r )  
         p   =   c o m p u t e p a y ( h o u r , r a t e )  
         p r i n t   ( p )  
 e x c e p t :  
         p r i n t   ( " P l e a s e , i n p u t   y o u r   n u m b e r i c " )  
 