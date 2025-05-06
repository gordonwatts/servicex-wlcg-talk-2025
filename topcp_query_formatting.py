query = (
    '{"reco": "CommonServices:\\n  systematicsHistogram: \'listOfSystematics\'\\n\\n'
    "PileupReweighting: {}\\n\\nEventCleaning:\\n    runEventCleaning: False\\n"
    "    runGRL: False\\n\\nElectrons:\\n  - containerName: 'AnaElectrons'\\n"
    "    crackVeto: True\\n    IFFClassification: {}\\n    WorkingPoint:\\n"
    "      - selectionName: 'loose'\\n        identificationWP: 'TightLH'\\n"
    "        isolationWP: 'NonIso'\\n        noEffSF: True\\n"
    "      - selectionName: 'tight'\\n        identificationWP: 'TightLH'\\n"
    "        isolationWP: 'Tight_VarRad'\\n        noEffSF: True\\n"
    "    PtEtaSelection:\\n        minPt: 25000.0\\n        maxEta: 2.47\\n"
    "        useClusterEta: True\\n\\n"
    "# After configuring each container, many variables will be saved automatically.\\n"
    "Output:\\n  treeName: 'reco'\\n  vars: []\\n  metVars: []\\n  containers:\\n"
    "      # Format should follow: '<suffix>:<output container>'\\n"
    "      el_: 'AnaElectrons'\\n      '': 'EventInfo'\\n  commands:\\n"
    "    # Turn output branches on and off with 'enable' and 'disable'\\n\\n"
    'AddConfigBlocks: []\\n", "parton": null, "particle": null, "max_events": 100, '
    '"no_systematics": true, "no_filter": false}'
)
