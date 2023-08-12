import streamlit as st
import streamlit.components.v1 as components

def main():
    st.set_page_config(page_title="E Hemanth Nagesh",
                       page_icon="",layout="wide")
    print(st.__path__)
    
    components.html("""<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Right Resume</title>
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="crossorigin"/>
    <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Poppins:wght@600&amp;family=Roboto:wght@300;400;500;700&amp;display=swap"/>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@600&amp;family=Roboto:wght@300;400;500;700&amp;display=swap" media="print" onload="this.media='all'"/>
    <noscript>
      <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@600&amp;family=Roboto:wght@300;400;500;700&amp;display=swap"/>
    </noscript>
    <link href="css/font-awesome/css/all.min.css?ver=1.2.0" rel="stylesheet">
    <link href="css/bootstrap.min.css?ver=1.2.0" rel="stylesheet">
    <link href="css/aos.css?ver=1.2.0" rel="stylesheet">
    <link href="css/main.css?ver=1.2.0" rel="stylesheet">
    <noscript>
      <style type="text/css">
        [data-aos] {
            opacity: 1 !important;
            transform: translate(0) scale(1) !important;
        }
      </style>
    </noscript>
  </head>
  <body id="top">
    <header class="d-print-none">
      <div class="container text-center text-lg-left">
        <div class="py-3 clearfix">
          <h1 class="site-title mb-0">E Hemanth Nagesh</h1>
          <div class="site-nav">
            <nav role="navigation">
              <ul class="nav justify-content-center">
                <li class="nav-item"><a class="nav-link" href="https://twitter.com/Nageshehemanth?t=u6n7yBv9gX13IJcDSCk22g&s=08" title="Twitter"><i class="fab fa-twitter"></i><span class="menu-title sr-only">Twitter</span></a>
                </li>
                <li class="nav-item"><a class="nav-link" href="https://m.facebook.com/profile.php?id=100004305736775" title="Facebook"><i class="fab fa-facebook"></i><span class="menu-title sr-only">Facebook</span></a>
                </li>
                <li class="nav-item"><a class="nav-link" href="https://instagram.com/__hemanth__beast_?igshid=MzNlNGNkZWQ4Mg==" title="Instagram"><i class="fab fa-instagram"></i><span class="menu-title sr-only">Instagram</span></a>
                </li>
                <li class="nav-item"><a class="nav-link" href="https://github.com/hemanth-nagesh" title="Github"><i class="fab fa-github"></i><span class="menu-title sr-only">Github</span></a>
                </li>
              </ul>
            </nav>
          </div>
        </div>
      </div>
    </header>
    <div class="page-content">
      <div class="container">
<div class="cover shadow-lg bg-white">
  <div class="cover-bg p-3 p-lg-4 text-white">
    <div class="row">
      <div class="col-lg-4 col-md-5">
        <div class="avatar hover-effect bg-white shadow-sm p-1"><img src="images/avatar.jpg" width="200" height="200"/></div>
      </div>
      <div class="col-lg-8 col-md-7 text-center text-md-start">
        <h2 class="h1 mt-2" data-aos="fade-left" data-aos-delay="0">E Hemanth Nagesh</h2>
        <p data-aos="fade-left" data-aos-delay="100">Software Engigeer & Web Developer</p>
        <div class="d-print-none" data-aos="fade-left" data-aos-delay="200"><a class="btn btn-light text-dark shadow-sm mt-1 me-1" href="right-resume.pdf" target="_blank">Download Resume</a></div>
      </div>
    </div>
  </div>
  <div class="about-section pt-4 px-3 px-lg-4 mt-1">
    <div class="row">
      <div class="col-md-6">
        <h2 class="h3 mb-3">About Me</h2>
        <p>Hello! I am E Hemanth Nagesh. I am passionate about Software design and Web Design. Highly skilled and detail-oriented Software Engineer in designing and developing innovative software solutions. Seeking a challenging position to leverage my technical expertise and passion for creating efficient and scalable applications.</p>
      </div>
      <div class="col-md-5 offset-md-1">
        <div class="row mt-2">
          <div class="col-sm-4">
            <div class="pb-1">Age</div>
          </div>
          <div class="col-sm-8">
            <div class="pb-1 text-secondary">23</div>
          </div>
          <div class="col-sm-4">
            <div class="pb-1">Email</div>
          </div>
          <div class="col-sm-8">
            <div class="pb-1 text-secondary">hemanthnagesh082@gmail.com</div>
          </div>
          <div class="col-sm-4">
            <div class="pb-1">Phone</div>
          </div>
          <div class="col-sm-8">
            <div class="pb-1 text-secondary">+91-99801-44503</div>
          </div>
          <div class="col-sm-4">
            <div class="pb-1">Address</div>
          </div>
          <div class="col-sm-8">
            <div class="pb-1 text-secondary">#28/1 20th cross, Cubbonpet, Bangaluru, katakana</div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <hr class="d-print-none"/>
  <div class="skills-section px-3 px-lg-4">
    <h2 class="h3 mb-3">Professional Skills</h2>
    <div class="row">
      <div class="col-md-6">
        <div class="mb-2"><span>Python</span>
          <div class="progress my-1">
            <div class="progress-bar bg-primary" role="progressbar" data-aos="zoom-in-right" data-aos-delay="100" data-aos-anchor=".skills-section" style="width: 80%" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
        </div>
        <div class="mb-2"><span>C/C++</span>
          <div class="progress my-1">
            <div class="progress-bar bg-primary" role="progressbar" data-aos="zoom-in-right" data-aos-delay="200" data-aos-anchor=".skills-section" style="width: 85%" aria-valuenow="85" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
        </div>
        <div class="mb-2"><span>JavaScript</span>
          <div class="progress my-1">
            <div class="progress-bar bg-primary" role="progressbar" data-aos="zoom-in-right" data-aos-delay="300" data-aos-anchor=".skills-section" style="width: 75%" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="mb-2"><span>HTML & CSS</span>
          <div class="progress my-1">
            <div class="progress-bar bg-success" role="progressbar" data-aos="zoom-in-right" data-aos-delay="400" data-aos-anchor=".skills-section" style="width: 80%" aria-valuenow="90" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
        </div>
        <div class="mb-2"><span>SQL/NO-SQL</span>
          <div class="progress my-1">
            <div class="progress-bar bg-success" role="progressbar" data-aos="zoom-in-right" data-aos-delay="600" data-aos-anchor=".skills-section" style="width: 70%" aria-valuenow="70" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <hr class="d-print-none"/>
  <div class="page-break"></div>
  <div class="education-section px-3 px-lg-4 pb-4">
    <h2 class="h3 mb-4">Education</h2>
    <div class="timeline">
      <div class="timeline-card timeline-card-success card shadow-sm">
        <div class="card-body">
          <div class="h5 mb-1">Master of Computer application <span class="text-muted h6">from PES College of Engineering</span></div>
          <div class="text-muted text-small mb-2">2021 - 2023</div>
          <div>GPA : 8.10/10</div>
        </div>
      </div>
      <div class="timeline-card timeline-card-success card shadow-sm">
        <div class="card-body">
          <div class="h5 mb-1">Bachelor of Computer application <span class="text-muted h6">from Ramaiah College</span></div>
          <div class="text-muted text-small mb-2">2007 - 2011</div>
          <div>Percentage: 75.00%</div>
        </div>
      </div>
      <div class="timeline-card timeline-card-success card shadow-sm">
        <div class="card-body">
          <div class="h5 mb-1">Software Testing <span class="text-muted h6">from NPTL</span></div>
          <div class="text-muted text-small mb-2">2022</div>
          <div>Completed an 8-week intensive course on software testing, enhancing proficiency in quality assurance and testing methodologies.</div>
        </div>
      </div>
    </div>
  </div>
  <hr class="d-print-none"/>
  <div class="work-experience-section px-3 px-lg-4">
    <h2 class="h3 mb-4">Internship</h2>
    <div class="timeline">
      <div class="timeline-card timeline-card-primary card shadow-sm">
        <div class="card-body">
          <div class="h5 mb-1">Botsio Chatbot LLP <span class="text-muted h6">at Mysore</span></div>
          <div class="text-muted text-small mb-2">2 - Months</div>
          <div>During my internship, I actively contributed to AI projects, including document and web scraping utilizing OpenAI API keys and word embeddings for enhanced data analysis and user engagement.</div>
        </div>
      </div>
    </div>
  </div>
  <hr class="d-print-none"/>
  <div class="page-break"></div>
  <div class="education-section px-3 px-lg-4 pb-4">
    <h2 class="h3 mb-4">projects</h2>
    <div class="timeline">
      <div class="timeline-card timeline-card-success card shadow-sm">
        <div class="card-body">
          <div class="h5 mb-1">DocuBot System Using AI <span class="text-muted h6">Python, HTML & CSS, No-SQL</span></div>
          <div>Designed a web page that allows user to upload their documents and system acts as a chatbot for user documents by providing username and password.</div>
        </div>
      </div>
      <div class="timeline-card timeline-card-success card shadow-sm">
        <div class="card-body">
          <div class="h5 mb-1">E-Learning website   <span class="text-muted h6">HTML, CSS, JavaScript & SQL</span></div>
          <div>Designed a web page that allows user to learn/take courses online by providing username and password </div>
        </div>
      </div>
    </div>
  </div>
  <hr class="d-print-none"/>
  <div class="contant-section px-3 px-lg-4 pb-4" id="contact">
    <h2 class="h3 text mb-3">Contact</h2>
    <div class="row">
      <div class="col-md-7 d-print-none">
        <div class="my-2"><form action="https://formsubmit.co/hemanthnageshintern@gmail.com"
    method="POST">
  <div class="row">
    <div class="col-6">
      <input class="form-control" type="text" id="name" name="name" placeholder="Your Name" required>
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_template" value="table">
    </div>
    <div class="col-6">
      <input class="form-control" type="email" id="email" name="email" placeholder="Your E-mail" required>
    </div>
  </div>
  <div class="form-group my-2">
    <textarea class="form-control" style="resize: none;" id="message" name="message" rows="4"  placeholder="Your Message" required></textarea>
  </div>
  <button class="btn btn-primary mt-2" type="submit">Send</button>
</form>
        </div>
      </div>
      <div class="col">
        <div class="mt-2">
          <h3 class="h6">Address</h3>
          <div class="pb-2 text-secondary">#28/1 20th cross, Cubbonpet, Bangaluru, katakana</div>
          <h3 class="h6">Phone</h3>
          <div class="pb-2 text-secondary">+91-9980144503</div>
          <h3 class="h6">Email</h3>
          <div class="pb-2 text-secondary">hemanthnagesh082@gmail.com</div>
        </div>
      </div>
      <div class="col d-none d-print-block">
        <div class="mt-2">
          <div>
            <div class="mb-2">
              <div class="text-dark"><i class="fab fa-twitter mr-1"></i><span>https://twitter.com/Nageshehemanth?t=u6n7yBv9gX13IJcDSCk22g&s=08</span>
              </div>
            </div>
            <div class="mb-2">
              <div class="text-dark"><i class="fab fa-facebook mr-1"></i><span>https://m.facebook.com/profile.php?id=100004305736775</span>
              </div>
            </div>
            <div class="mb-2">
              <div class="text-dark"><i class="fab fa-instagram mr-1"></i><span>https://instagram.com/__hemanth__beast_?igshid=MzNlNGNkZWQ4Mg==</span>
              </div>
            </div>
            <div class="mb-2">
              <div class="text-dark"><i class="fab fa-github mr-1"></i><span>https://github.com/hemanth-nagesh</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div></div>
    </div>
    <footer class="pt-4 pb-4 text-muted text-center d-print-none">
      <div class="container">
        <div class="my-3">
          <div class="h4">E Hemanth Nagesh</div>
          <div class="footer-nav">
            <nav role="navigation">
              <ul class="nav justify-content-center">
                <li class="nav-item"><a class="nav-link" href="https://twitter.com/Nageshehemanth?t=u6n7yBv9gX13IJcDSCk22g&s=08" title="Twitter"><i class="fab fa-twitter"></i><span class="menu-title sr-only">Twitter</span></a>
                </li>
                <li class="nav-item"><a class="nav-link" href="https://m.facebook.com/profile.php?id=100004305736775" title="Facebook"><i class="fab fa-facebook"></i><span class="menu-title sr-only">Facebook</span></a>
                </li>
                <li class="nav-item"><a class="nav-link" href="https://instagram.com/__hemanth__beast_?igshid=MzNlNGNkZWQ4Mg==" title="Instagram"><i class="fab fa-instagram"></i><span class="menu-title sr-only">Instagram</span></a>
                </li>
                <li class="nav-item"><a class="nav-link" href="https://github.com/hemanth-nagesh" title="Github"><i class="fab fa-github"></i><span class="menu-title sr-only">Github</span></a>
                </li>
              </ul>	
            </nav>
          </div>
        </div>
        <div class="text-small">
          <div class="mb-1">&copy; Right Resume. All rights reserved.</div>
        </div>
      </div>
    </footer>
    <script src="scripts/bootstrap.bundle.min.js?ver=1.2.0"></script>
    <script src="scripts/aos.js?ver=1.2.0"></script>
    <script src="scripts/main.js?ver=1.2.0"></script>
  </body>
</html>""", width=1900, height=3500)
    #st.write(resume,unsafe_allow_html=True)
if __name__ == '__main__':
    main()
