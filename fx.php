<?php for ($i = 100; $i <= 130; $i++): ?>
  job_<?php echo $i ?>:
    JobeetCategory: programming
    company:      Company <?php echo $i."\n" ?>
    position:     Web Developer
    location:     Paris, France
    description:  Lorem ipsum dolor sit amet, consectetur adipisicing elit.
    how_to_apply: |
      Send your resume to lorem.ipsum [at] company_<?php echo $i ?>.sit
    is_public:    true
    is_activated: true
    token:        job_<?php echo $i."\n" ?>
    email:        job@example.com
 
<?php endfor ?>