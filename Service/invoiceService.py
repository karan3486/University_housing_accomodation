from Model.model import Invoice
from Repository.invoiceRepository import InvoiceRepository
from Serializer.serializer import  InvoiceSerializer
from Logger.logger import get_logger
from Utilities.utilities import RESIDENCE_TYPE

class InvoiceServices:
    def __init__(self) -> None:
        self.invoice_repository = InvoiceRepository()
        self.logger = get_logger()

    def create(self, invoice):
        try:
            deserializedData = InvoiceSerializer().load(invoice)
            invoiceModel = Invoice(**deserializedData)
            id = self.invoice_repository.get_max_id()
            invoiceModel.invoiceid = id
            new_invoice=self.invoice_repository.save(invoiceModel)
            if new_invoice:
                deserializedData['invoiceid'] = id
                return InvoiceSerializer().dump(deserializedData)
            else:
                return new_invoice
        except Exception as e:
            self.logger.error("Error while creating a new Invoice : {}".format(e))
            return False
        
    def updateInvoice(self,invoice):
        try:
            deserializedData = InvoiceSerializer().load(invoice)
            invoicenewModel = Invoice(**deserializedData)
            invoiceoldModel = self.invoice_repository.get_by_id(invoicenewModel.invoiceid)
            new_invoice=self.invoice_repository.update(invoiceoldModel,invoicenewModel)
            if new_invoice:
                return InvoiceSerializer().dump(deserializedData)
            else:
                return new_invoice
        except Exception as e:
            self.logger.error("Error while creating a new invoice : {}".format(e))
            return False

    def get_invoice_detail(self,id:int):
        try:
            invoiceDetail = self.invoice_repository.get_by_id(id)
            invoiceDetail = InvoiceSerializer().dump(invoiceDetail)
            return invoiceDetail
        except Exception as e:
            self.logger.info("Error while getting all invoices : ",e)

    def delete_invoice(self,id:int):
        try:
            isdelete = self.invoice_repository.delete(id)
            return isdelete
        except Exception as e:
            self.logger.info("Error while getting all invoices : ",e)

    def get_all_invoiceList(self):
        try:
            invoicelistdata =  self.invoice_repository.get_all()
            invoicelist = [InvoiceSerializer().dump(data) for data in invoicelistdata]
            return invoicelist
        except Exception as e:
            self.logger.info("Error while getting all invoices : ",e)