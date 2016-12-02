from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, RequestContext
import matplotlib
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
import os.path
import inspect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from blog.models import Document 
from blog.forms import DocumentForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import views



rate = 0
file = 0
file_path = 0

def main (request):
    return render_to_response('blog/main.html')           
 
	
def main_chart (request):
    
    #global rate 
    #rate = request.POST.get['d', ""] 
    
    #global file
    #file = request.GET['file']

    global file_path
	
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    file_path = os.path.join(MEDIA_ROOT, file)
	
    return render_to_response('blog/main_chart.html')   
	
def post_list(request):
  
	
    #Ts = 1.0/Fs; # sampling interval
    #ff = 50;   # frequency of the signal	    
    #y = np.sin(2*np.pi*ff*t) 
    
	
    with open(file_path) as file: # open and separate per line 
        array = [row.strip() for row in file]
    
    y = [float(i) for i in array] # parse string to float
	
    n = len(y) # length of the signal
    t = np.arange(0,n,1) # time vector    
	
    Fs = float(rate);  # sampling rate  	
	
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
	
def sample_freq(sample_freq):
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()   
    op = showinfo("Say Hello", sample_freq)      
    root.mainloop()   
	


def upload_file(request):

     global rate
     global file
	 
     form = DocumentForm(request.POST, request.FILES)
     
     if form.is_valid():
          rate = form.cleaned_data['description']
          file = form.cleaned_data['document'].name
     if form.is_valid():
	      form.save()          
	      return HttpResponseRedirect(reverse('main_chart')) 
     else:
	      form = DocumentForm()
	 
     return render(request, 'blog/add_data.html', {'form': form}, context_instance=RequestContext(request)) 
    


