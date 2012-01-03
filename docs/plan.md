content:
        bio
        cv
        resume
        networks
                github
                fb
                twitter
                g+
                
        portfolio
                robotics
                        <list you sent to anybots>
                other projects

        blog
                <all existing blog entries>

design goals:
        page heiarchy
        url control
        navigation
        write all content in markdown
        blog
        parts are controllable

compilation process for single page
  generate markdown if necessary
  run markdown on everything
  assemble with parts

normal page structure
  (folder) something
    (file) index.md --> special, defines page for top level page for <something> page
    (file) other thing.md --> normal page under <something>
    
blog structure
  (folder) blog --> special
    (file) index.md --> most recent posts, automatically generated
    (file) index1.md --> next page of posts, automatically generated
    ...
    (file) indexN.md --> last page of summaries, automatically generated
    (folder) posts
      (file) index.md --> automatically generated list of all posts
      (file) post1.md (name could be anything) (ordered by date modified)
      ...
      (file) post\_whatever.md (name could be anything) (ordered by date modified)

