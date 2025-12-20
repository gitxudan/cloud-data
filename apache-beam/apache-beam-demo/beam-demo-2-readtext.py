import apache_beam as beam

with beam.Pipeline() as pipeline:
    Pcollection =(
        pipeline
        | "import data from customer">> beam.io.ReadFromText("data/customer_5.txt",
                                                               skip_header_lines=1)   
        | "split by tab" >> beam.Map(lambda record: record.split("\t"))
       # | beam.Map(lambda record: record[:2]+  
                   
         #          )  # flatten the list
        | "print data" >> beam.Map(print)
    )
    #pipeline.run() #build your pipeline here