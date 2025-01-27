import { ApplicationService, CompanyService, connectToDatabase } from '@ponti/utils'

export async function POST(req: Request) {
  const db = await connectToDatabase()
  const applicationService = new ApplicationService({ db })
  const companyService = new CompanyService({ db })
  const data = await req.json()
  const company = await companyService.findById(data.companyId)

  if (!company) {
    return Response.json({ error: 'Company not found' }, { status: 404 })
  }

  const applicationId = await applicationService.create({
    jobId: data.jobId,
    userId: data.userId,
    status: 'pending',
    resume: data.resume,
    coverLetter: data.coverLetter,
    companyId: company._id,
  })

  const application = await applicationService.findById(applicationId.toString())
  return Response.json(application, { status: 201 })
}

export async function PUT(req: Request) {
  const db = await connectToDatabase()
  const applicationService = new ApplicationService({ db })

  const { id, ...data } = await req.json()

  const success = await applicationService.update(id, data)

  if (!success) {
    return Response.json({ error: 'Application not found' }, { status: 404 })
  }

  const updated = await applicationService.findById(id)
  return Response.json(updated, { status: 200 })
}

export async function GET(req: Request) {
  const db = await connectToDatabase()
  const applicationService = new ApplicationService({ db })

  const { searchParams } = new URL(req.url)
  const id = searchParams.get('id')

  if (id) {
    const application = await applicationService.findById(id)
    if (!application) {
      return Response.json({ error: 'Application not found' }, { status: 404 })
    }
    return Response.json(application)
  }

  const applications = await applicationService.findMany()
  return Response.json(applications)
}

export async function DELETE(req: Request) {
  const db = await connectToDatabase()
  const applicationService = new ApplicationService({ db })

  const { searchParams } = new URL(req.url)
  const id = searchParams.get('id')

  if (!id) {
    return Response.json({ error: 'ID is required' }, { status: 400 })
  }

  const success = await applicationService.delete(id)
  if (!success) {
    return Response.json({ error: 'Application not found' }, { status: 404 })
  }

  return new Response(null, { status: 204 })
}
