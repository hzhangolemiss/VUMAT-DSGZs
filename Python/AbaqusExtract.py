#!/usr/bin/env python

import odbAccess

class AbaqusExtract:

    def __init__(self, name):
        self.filename = name
        self.run()
        self.run_c()

    def fileHistory(self, history):
        time = []
        position = []
        for tm, pos in history:
            time.append(tm)
            position.append(pos)
        return time, position

    def rawReadLineNumber(self, file, number):
        FRead = open(file, "r")
        lines = FRead.readlines()
        FRead.close()
        return lines[number-1]

    def rawRead(self, file):
        FRead = open(file, "r")
        lines = FRead.readlines()
        FRead.close()
        lines = [x.partition('#')[0] for x in lines if (x and x.partition('#')[0])]
        return lines

    def run(self):
        dataJobs = []
        dataValues = []
        dataNames = []
        dataRegions = []
        dataOperates = []
        lines = self.rawRead(self.filename)
        for line in lines:
            # split and strip line
            lineItems = [x.strip() for x in line.split(',')]
            # extract parameters
            if (lineItems[0] == 'TimeHistory'):
                dataOperates.append('none')
                for item in lineItems:
                    item = [x.strip() for x in item.split('=')]
                    if (item[0] == 'job'): dataJobs.append(item[1])
                    if (item[0] == 'value'): dataValues.append(item[1])
                    if (item[0] == 'name'): dataNames.append(item[1])
                    if (item[0] == 'region'):
                        if '+' in item[1]:
                            # many regions
                            group = [x.strip() for x in item[1].split('+')]
                            dataRegions.append(group)
                        else:
                            # one region
                            reg = []
                            reg.append(item[1])
                            dataRegions.append(reg)
                    if (item[0] == 'operate'): dataOperates[-1] = item[1]
        #print(dataJobs)
        #print(dataValues)
        #print(dataNames)
        #print(dataRegions)
        #print(dataOperates)
        #print(dataOperates[0])
        #print(len(dataJobs))
        #print(len(dataValues))
        #print(len(dataNames))
        #print(len(dataRegions))
        for var in range (0, len(dataJobs)):
            # get the odb object
            jobFile = dataJobs[var]
            odb = odbAccess.openOdb(path = jobFile+".odb")
            # get the step 1
            step1 = odb.steps['Step-1']
            outFile = jobFile+'_'+dataNames[var]+'.plot'
            dispFile = open(outFile,'w')
            nbPts = len(dataRegions[var])
            if (nbPts == 1):
                print("Extracting "+dataNames[var]+" from "+jobFile+".odb")
                dispFile.write("#DynELA_plot :"+jobFile+'_'+dataNames[var]+'\n')
                dispFile.write("#plotted :"+jobFile+'_'+dataNames[var]+'\n')
                region = step1.historyRegions[dataRegions[var][0]]
                time, data = self.fileHistory(region.historyOutputs[dataValues[var]].data)
                for i in range (0, len(time)):
                    dispFile.write(str(time[i])+" "+str(data[i])+'\n')
            elif (dataOperates[var] == 'none'):
                print("Extracting multiple "+str(nbPts)+" values for "+dataNames[var]+" from "+jobFile+".odb")
                dispFile.write("#DynELA_plot :"+jobFile+'_'+dataNames[var]+'\n')
                dispFile.write("#plotted :")
                for pt in range (0, nbPts):
                    dispFile.write(jobFile+'_'+dataNames[var]+'_'+str(pt)+' ')
                dispFile.write('\n')
                datas = []
                for pt in range (0, nbPts):
                    region = step1.historyRegions[dataRegions[var][pt]]
                    time, data = self.fileHistory(region.historyOutputs[dataValues[var]].data)
                    datas.append(data)
                for i in range (0, len(time)):
                    dispFile.write(str(time[i]))
                    for pt in range (0, nbPts):
                        dispFile.write(" "+str(datas[pt][i]))
                    dispFile.write('\n')
            else:
                print("Combining "+str(nbPts)+" values for "+dataNames[var]+" from "+jobFile+".odb")
                dispFile.write("#DynELA_plot :"+jobFile+'_'+dataNames[var]+'\n')
                dispFile.write("#plotted :"+jobFile+'_'+dataNames[var]+'\n')
                datas = []
                for pt in range (0, nbPts):
                    region = step1.historyRegions[dataRegions[var][pt]]
                    time, data = self.fileHistory(region.historyOutputs[dataValues[var]].data)
                    datas.append(data)
                data = []
                for dat in range(len(time)):
                    if (dataOperates[var] == 'mean'):
                        d = 0.0
                        for pt in range (0, nbPts): d += datas[pt][dat]
                        data.append(d/nbPts)
                    if (dataOperates[var] == 'sum'):
                        d = 0.0
                        for pt in range (0, nbPts): d += datas[pt][dat]
                        data.append(d)
                for i in range (0, len(time)):
                    dispFile.write(str(time[i])+" "+str(data[i])+'\n')
            dispFile.close()

    def run_c(self):
        dataJobs = []
        dataValues = []
        dataNames = []
        dataRegions = []
        dataOperates = []
        lines = self.rawRead(self.filename)
        for line in lines:
            # split and strip line
            lineItems = [x.strip() for x in line.split(',')]
            # extract parameters
            if (lineItems[0] == 'DataCombine'):
                dataOperates.append('none')
                for item in lineItems:
                    item = [x.strip() for x in item.split('=')]
                    if (item[0] == 'job'): dataJobs.append(item[1])
                    if (item[0] == 'value'): dataValues.append(item[1])
                    if (item[0] == 'name'): dataNames.append(item[1])
                    if (item[0] == 'region'):
                        if '+' in item[1]:
                            # many regions
                            group = [x.strip() for x in item[1].split('+')]
                            dataRegions.append(group)
                        else:
                            # one region
                            reg = []
                            reg.append(item[1])
                            dataRegions.append(reg)
                    if (item[0] == 'operate'): dataOperates[-1] = item[1]
        #print(dataJobs)
        #print(dataValues)
        #print(dataNames)
        #print(dataRegions)
        #print(dataOperates)
        #print(dataOperates[0])
        #print(len(dataJobs))
        #print(len(dataValues))
        #print(len(dataNames))
        #print(len(dataRegions))
        for var in range (0, len(dataJobs)):
            # get the odb object
            jobFile = dataJobs[var]
            odb = odbAccess.openOdb(path = jobFile+".odb")
            # get the step 1
            step1 = odb.steps['Step-1']
            outFile = jobFile+'_'+dataNames[2*var]+'_'+dataNames[2*var+1]+'.plot'
            dispFile = open(outFile,'w')
            nbPts = len(dataRegions[var])
            if (nbPts == 1):
                print("Extracting "+dataNames[2*var]+" and "+dataNames[2*var+1]+" from "+jobFile+".odb")
                dispFile.write("#DynELA_plot :"+jobFile+'_'+dataNames[2*var]+'_'+dataNames[2*var+1]+'\n')
                dispFile.write("#plotted :"+jobFile+'_'+dataNames[2*var]+'_'+dataNames[2*var+1]+'\n')
                region = step1.historyRegions[dataRegions[var][0]]
                time1, data1 = self.fileHistory(region.historyOutputs[dataValues[2*var]].data)
                time2, data2 = self.fileHistory(region.historyOutputs[dataValues[2*var+1]].data)
                if (time1 == time2):
                    for i in range (0, len(time1)):
                        dispFile.write(str(data1[i])+" "+str(data2[i])+'\n')
            #elif (dataOperates[var] == 'none'):
                #print("Extracting multiple "+str(nbPts)+" values for "+dataNames[var]+" from "+jobFile+".odb")
                #dispFile.write("#DynELA_plot: "+jobFile+'_'+dataNames[var]+'\n')
                #dispFile.write("#plotted: ")
                #for pt in range (0, nbPts):
                #    dispFile.write(jobFile+'_'+dataNames[var]+'_'+str(pt)+' ')
                #dispFile.write('\n')
                #datas = []
                #for pt in range (0, nbPts):
                #    region = step1.historyRegions[dataRegions[var][pt]]
                #    time, data = self.fileHistory(region.historyOutputs[dataValues[var]].data)
                #    datas.append(data)
                #for i in range (0, len(time)):
                #    dispFile.write(str(time[i]))
                #    for pt in range (0, nbPts):
                #        dispFile.write(" "+str(datas[pt][i]))
                #    dispFile.write('\n')
            #else:
                #print("Combining "+str(nbPts)+" values for "+dataNames[var]+" from "+jobFile+".odb")
                #dispFile.write("#DynELA_plot: "+jobFile+'_'+dataNames[var]+'\n')
                #dispFile.write("#plotted: "+jobFile+'_'+dataNames[var]+'\n')
                #datas = []
                #for pt in range (0, nbPts):
                #    region = step1.historyRegions[dataRegions[var][pt]]
                #    time, data = self.fileHistory(region.historyOutputs[dataValues[var]].data)
                #    datas.append(data)
                #data = []
                #for dat in range(len(time)):
                #    if (dataOperates[var] == 'mean'):
                #        d = 0.0
                #        for pt in range (0, nbPts): d += datas[pt][dat]
                #        data.append(d/nbPts)
                #    if (dataOperates[var] == 'sum'):
                #        d = 0.0
                #        for pt in range (0, nbPts): d += datas[pt][dat]
                #        data.append(d)
                #for i in range (0, len(time)):
                #    dispFile.write(str(time[i])+" "+str(data[i])+'\n')
            dispFile.close()

# extract data
AbaqusExtract('../Extract.ex')
