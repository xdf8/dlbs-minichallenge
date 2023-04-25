# dlbs-minichallenge

## Übersicht

### Fragestellung

Lassen sich Automarken- und -modelle mittels Bilderkennung kategorisieren?

- Objekterkennung
  - Automarken- und -modell-Erkennung, um Gewicht aller Autos im Autoverlad auf einem Zugabteil einschätzen zu können, hat (unter anderem) Auswirkungen auf den Verschleiss.
- Datenlage
  - [Stanford Car Data](http://ai.stanford.edu/~jkrause/cars/car_dataset.html): Make and Model (US Dataset, bereinigt für Schweizer Verhältnisse)
- Methode
  - Baseline: Transfer learning auf YOLOv7
  - DL Architektur: [YOLOv7](https://github.com/WongKinYiu/yolov7) (Baseline), [SAM](https://segment-anything.com) (Fabian), [Mask R-CNN](https://github.com/matterport/Mask_RCNN) (Eric)
  - Evaluation: F1-Score


## Eigenes bBewertungskriterium

- **Ergebnisse und Schlussfolgerungen**
  - Qualität der Analyseergebnisse: Wie präzise und zuverlässig sind die Ergebnisse der Modellierung? Wurden angemessene Metriken verwendet?
  - Relevanz der Schlussfolgerungen: Sind die Schlussfolgerungen aus den Ergebnissen angemessen und logisch? Haben sie einen direkten Bezug zur Fragestellung?
  - Konsistenz der Ergebnisse: Stimmen die Ergebnisse mit den Erwartungen überein und sind sie in sich schlüssig?
  - Präsentation der Ergebnisse: Sind die Ergebnisse klar und verständlich präsentiert und werden sie durch geeignete Visualisierungen unterstützt?
  - (Implikationen der Ergebnisse: Werden die Auswirkungen der Ergebnisse auf den Kontext der Fragestellung und den Forschungsbereich angemessen diskutiert?)
