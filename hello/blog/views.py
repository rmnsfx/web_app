from django.shortcuts import render
from django.http import HttpResponse

#def post_list(request):
#    return render(request, 'blog/post_list.html', {})

import matplotlib.pyplot as plt
import numpy as np
from pylab import figure, axes, pie, title
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.shortcuts import render_to_response
import io
from io import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import fileinput
import threading
import matplotlib
matplotlib.use('Agg')

def main (request):
    return render_to_response('blog/main.html')          
	
def add_data (request):
    return render_to_response('blog/add_data.html')  
	
def main_chart (request):
    return render_to_response('blog/main_chart.html')  
	
def post_list(request):

    Fs = 150.0;  # sampling rate
    Ts = 1.0/Fs; # sampling interval
    ff = 50;   # frequency of the signal
	
    t = np.arange(0,1,Ts) # time vector    
    y = np.sin(2*np.pi*ff*t) 

    n = len(y) # length of the signal
    k = np.arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range
    frq = frq[0:n/2] # one side frequency range

    Y = np.fft.fft(y)/n # fft computing and normalization
    Y = Y[0:n/2] 
    
    fig, ax = plt.subplots(2, 1, figsize=(10,10))
    fig.patch.set_facecolor('white')
	
    ax[0].plot(t,y)
    ax[0].set_xlabel('Time')
    ax[0].set_ylabel('Amplitude')
	
    ax[1].plot(frq,abs(Y),'r') # plotting the spectrum
    ax[1].set_xlabel('Freq (Hz)')
    ax[1].set_ylabel('|Y(freq)|')
		
    canvas = FigureCanvasAgg(fig)     
    response = HttpResponse(content_type='image/png')    
    canvas.print_png(response)  
	    	
    plt.close()	
	
    return response           
    #return render(request, 'blog/post_list.html', {'response': response})
    #return render_to_response('blog/post_list.html', {'response': response})
    #return HttpResponse (response.getvalue(), content_type="Image/png")
	#response = io.BytesIO()    
	#plt.savefig('img.png')
	#fig = plt.figure()
    #scatter1 = plt.scatter(0.0, 1.0)
    #graph1 = plt.plot([-1.0, 1.0], [0.0, 1.0])
	
def open_file(self):
	
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()
   
    op = askopenfile()      
    root.mainloop()
	
 
		
    #t = threading.Thread(target=callback)
    #t.daemon = False 
    #t.start()
	#root.deiconify()
    #root.lift()
    #root.focus_force() 
    